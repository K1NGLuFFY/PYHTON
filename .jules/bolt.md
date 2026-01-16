## 2024-05-22 - Deep Copy Performance
**Learning:** copy.deepcopy is significantly slower than json serialization for deep copying JSON-compatible data. For 1000 items, deepcopy took ~3.6s vs ~2.0s for json dump/load.
**Action:** Use json.loads(json.dumps(x)) for deep copying JSON data, or avoid copies entirely by returning references where safe (read-only paths).
