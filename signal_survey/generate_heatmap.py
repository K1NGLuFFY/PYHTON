import argparse
import sys
from typing import List, Tuple, Optional

# Lazy import heavy deps with clear errors
try:
    import pandas as pd
except ImportError as e:
    print("Missing dependency: pandas. Install with: pip install pandas", file=sys.stderr)
    raise

try:
    import folium
    from folium.plugins import HeatMap
except ImportError as e:
    print("Missing dependency: folium. Install with: pip install folium", file=sys.stderr)
    raise


def resolve_columns(df: 'pd.DataFrame') -> Tuple[str, str, str]:
    """
    Attempt to resolve latitude, longitude and signal (dBm) column names from common variants.
    Returns a tuple of (lat_col, lon_col, signal_col). Raises ValueError if not found.
    """
    lat_candidates = [
        'lat', 'latitude', 'Latitude', 'LAT', 'Lat', 'gps_latitude'
    ]
    lon_candidates = [
        'lon', 'lng', 'long', 'longitude', 'Longitude', 'LON', 'Lng', 'gps_longitude'
    ]
    signal_candidates = [
        'signal_dbm', 'rssi', 'RSSI', 'Signal_dBm', 'signal', 'level_dbm', 'dbm', 'RSRP', 'rsrp'
    ]

    def find_one(cands: List[str]) -> Optional[str]:
        for c in cands:
            if c in df.columns:
                return c
        # case-insensitive fallback
        lower_map = {c.lower(): c for c in df.columns}
        for c in cands:
            if c.lower() in lower_map:
                return lower_map[c.lower()]
        return None

    lat = find_one(lat_candidates)
    lon = find_one(lon_candidates)
    sig = find_one(signal_candidates)

    missing = []
    if not lat:
        missing.append('latitude')
    if not lon:
        missing.append('longitude')
    if not sig:
        missing.append('signal (dBm)')
    if missing:
        raise ValueError(
            f"Could not find required column(s): {', '.join(missing)}.\n"
            f"Available columns: {list(df.columns)}\n"
            f"Expected columns include: latitude/lat, longitude/lon, and signal_dbm/rssi/dbm."
        )
    return lat, lon, sig


def normalize_dbm_to_weight(dbm: float, min_dbm: float, max_dbm: float) -> float:
    """Map dBm to a [0,1] weight where 0 is weakest (<= min_dbm) and 1 is strongest (>= max_dbm)."""
    if dbm is None:
        return 0.0
    # Ensure numeric
    try:
        val = float(dbm)
    except Exception:
        return 0.0
    if max_dbm == min_dbm:
        return 0.0
    w = (val - min_dbm) / (max_dbm - min_dbm)
    if w < 0:
        w = 0.0
    if w > 1:
        w = 1.0
    return w


def default_gradient():
    """
    Return a gradient mapping for HeatMap weights from 0..1
    0 -> red (bad), 0.5 -> yellow, 1 -> green (good)
    """
    return {
        0.0: '#ff0000',
        0.25: '#ff6a00',
        0.5: '#ffd200',
        0.75: '#a8e05f',
        1.0: '#00b150',
    }


def build_map(points: List[Tuple[float, float, float]], dead_points: List[Tuple[float, float, float]],
              center: Tuple[float, float], tiles: str, radius: int, blur: int,
              gradient: dict) -> 'folium.Map':
    m = folium.Map(location=center, zoom_start=15, tiles=tiles)

    # Heat layer
    heat_data = [[lat, lon, weight] for (lat, lon, weight) in points]
    HeatMap(heat_data, radius=radius, blur=blur, max_zoom=18, gradient=gradient).add_to(m)

    # Dead zone markers
    if dead_points:
        fg = folium.FeatureGroup(name='Dead zones (below threshold)')
        for lat, lon, value in dead_points:
            folium.CircleMarker(
                location=(lat, lon),
                radius=4,
                color='#b10000',
                fill=True,
                fill_opacity=0.8,
                fill_color='#b10000',
                tooltip=f"dBm: {value}"
            ).add_to(fg)
        fg.add_to(m)

    folium.LayerControl().add_to(m)
    return m


def main():
    parser = argparse.ArgumentParser(description='Generate a signal coverage heatmap (Wi-Fi/Cellular) and highlight dead zones.')
    parser.add_argument('-i', '--input', required=True, help='Path to input CSV with latitude, longitude, and signal (dBm).')
    parser.add_argument('-o', '--output', required=False, default='coverage_heatmap.html', help='Output HTML map path.')
    parser.add_argument('--dead-threshold', type=float, default=-100.0, help='dBm threshold to flag dead/poor zones (e.g., -95).')
    parser.add_argument('--min-dbm', type=float, default=-110.0, help='Minimum dBm for normalization (weaker).')
    parser.add_argument('--max-dbm', type=float, default=-50.0, help='Maximum dBm for normalization (stronger).')
    parser.add_argument('--radius', type=int, default=16, help='Heat point radius.')
    parser.add_argument('--blur', type=int, default=24, help='Heat blur.')
    parser.add_argument('--tiles', type=str, default='OpenStreetMap', help='Base map tiles provider.')

    args = parser.parse_args()

    # Load CSV
    try:
        df = pd.read_csv(args.input)
    except Exception as e:
        print(f"Failed to read CSV: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        lat_col, lon_col, sig_col = resolve_columns(df)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(2)

    # Drop rows with missing coords or signal
    df = df[[lat_col, lon_col, sig_col]].dropna()

    # Ensure numeric
    df[lat_col] = pd.to_numeric(df[lat_col], errors='coerce')
    df[lon_col] = pd.to_numeric(df[lon_col], errors='coerce')
    df[sig_col] = pd.to_numeric(df[sig_col], errors='coerce')
    df = df.dropna()

    if df.empty:
        print("No valid rows after cleaning. Ensure your CSV has latitude, longitude, and signal dBm values.", file=sys.stderr)
        sys.exit(3)

    # Build points
    points: List[Tuple[float, float, float]] = []
    dead_points: List[Tuple[float, float, float]] = []

    for _, row in df.iterrows():
        lat = float(row[lat_col])
        lon = float(row[lon_col])
        dbm = float(row[sig_col])
        weight = normalize_dbm_to_weight(dbm, args.min_dbm, args.max_dbm)
        points.append((lat, lon, weight))
        if dbm <= args.dead_threshold:
            dead_points.append((lat, lon, dbm))

    # Center map on mean position
    center = (float(df[lat_col].mean()), float(df[lon_col].mean()))

    m = build_map(points, dead_points, center, args.tiles, args.radius, args.blur, default_gradient())

    try:
        m.save(args.output)
    except Exception as e:
        print(f"Failed to write output HTML: {e}", file=sys.stderr)
        sys.exit(4)

    print("Heatmap generated:", args.output)
    print(f"Points: {len(points)} | Dead/poor points (<= {args.dead_threshold} dBm): {len(dead_points)}")
    print("Tip: Adjust --min-dbm/--max-dbm to fit your dataset's range for better contrast.")


if __name__ == '__main__':
    main()
