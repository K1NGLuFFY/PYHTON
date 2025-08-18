# Stock Market Price Tracker

A modern, responsive web application for tracking stock market prices with interactive charts and watchlist functionality.

## Features

- **Real-time Stock Data**: Search and display current stock prices
- **Interactive Charts**: Beautiful line charts showing price history
- **Multiple Timeframes**: View data for 1D, 1W, 1M, 3M, and 1Y periods
- **Watchlist**: Save your favorite stocks for quick access
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Popular Stocks**: Quick access to popular stocks like AAPL, GOOGL, MSFT, TSLA, AMZN

## Demo Data

This application uses demo data for demonstration purposes. The following stocks are available:

- **AAPL** - Apple Inc.
- **GOOGL** - Alphabet Inc.
- **MSFT** - Microsoft Corporation
- **TSLA** - Tesla, Inc.
- **AMZN** - Amazon.com Inc.

## Getting Started

1. **Open the Application**: Simply open `index.html` in your web browser
2. **Search for Stocks**: Enter any stock symbol (try the demo symbols above)
3. **View Charts**: Click on different timeframes to see price history
4. **Build Watchlist**: Add stocks to your watchlist for quick access

## Real API Integration

To use real stock data instead of demo data:

1. **Get an API Key**: Sign up for a free API key at [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
2. **Update the Code**: Replace `const API_KEY = 'demo'` in `script.js` with your actual API key
3. **Enable Real Data**: Uncomment the real API calls in the `loadStock` function

### Real API Implementation

Replace the demo data section in `script.js` with:

```javascript
async function loadStock(symbol) {
    currentSymbol = symbol;
    showLoading();
    hideError();
    
    try {
        // Get quote data
        const quoteResponse = await fetch(`${API_BASE_URL}?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=${API_KEY}`);
        const quoteData = await quoteResponse.json();
        
        if (!quoteData['Global Quote']) {
            throw new Error('Invalid stock symbol');
        }
        
        // Get historical data
        const historyResponse = await fetch(`${API_BASE_URL}?function=TIME_SERIES_DAILY&symbol=${symbol}&apikey=${API_KEY}`);
        const historyData = await historyResponse.json();
        
        // Process and display data
        const stockData = processStockData(quoteData, historyData);
        displayStockData(stockData);
        renderChart(stockData.history);
        
    } catch (error) {
        showError(`Error loading stock data: ${error.message}`);
    } finally {
        hideLoading();
    }
}
```

## File Structure

```
stock-tracker/
├── index.html          # Main HTML file
├── styles.css          # CSS styles
├── script.js          # JavaScript functionality
└── README.md          # This documentation
```

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Technologies Used

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with flexbox and grid
- **JavaScript ES6+** - Modern JavaScript features
- **Chart.js** - Interactive charts
- **Font Awesome** - Icons
- **Local Storage** - Watchlist persistence

## Customization

### Styling
- Modify colors in `styles.css`
- Adjust layout and spacing
- Add dark mode support

### Features
- Add more technical indicators
- Implement portfolio tracking
- Add news integration
- Enable price alerts

### API Options
- **Alpha Vantage** (current) - Free tier with 5 calls/minute
- **Yahoo Finance** - Alternative data source
- **IEX Cloud** - Premium features
- **Polygon.io** - Real-time data

## Performance Notes

- Demo data loads instantly
- Real API calls may have slight delays
- Chart rendering is optimized for smooth animations
- Local storage keeps watchlist between sessions

## License

This project is open source and available under the MIT License.
