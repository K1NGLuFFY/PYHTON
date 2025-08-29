// API Configuration
const API_KEY = 'demo'; // Using demo data for this example
const API_BASE_URL = 'https://www.alphavantage.co/query';

// Global variables
let currentChart = null;
let currentSymbol = '';
let watchlist = JSON.parse(localStorage.getItem('stockWatchlist')) || [];

// Demo data for demonstration
const demoData = {
    'AAPL': {
        name: 'Apple Inc.',
        symbol: 'AAPL',
        price: 175.43,
        change: 2.15,
        changePercent: 1.24,
        marketCap: '2.8T',
        volume: '58.2M',
        dayHigh: 176.80,
        dayLow: 174.20,
        history: generateDemoHistory(175.43)
    },
    'GOOGL': {
        name: 'Alphabet Inc.',
        symbol: 'GOOGL',
        price: 142.65,
        change: -1.23,
        changePercent: -0.85,
        marketCap: '1.8T',
        volume: '28.5M',
        dayHigh: 144.10,
        dayLow: 141.90,
        history: generateDemoHistory(142.65)
    },
    'MSFT': {
        name: 'Microsoft Corporation',
        symbol: 'MSFT',
        price: 378.85,
        change: 3.42,
        changePercent: 0.91,
        marketCap: '2.9T',
        volume: '22.1M',
        dayHigh: 380.50,
        dayLow: 376.20,
        history: generateDemoHistory(378.85)
    },
    'TSLA': {
        name: 'Tesla, Inc.',
        symbol: 'TSLA',
        price: 238.45,
        change: -5.67,
        changePercent: -2.32,
        marketCap: '758B',
        volume: '45.8M',
        dayHigh: 245.30,
        dayLow: 237.10,
        history: generateDemoHistory(238.45)
    },
    'AMZN': {
        name: 'Amazon.com Inc.',
        symbol: 'AMZN',
        price: 178.35,
        change: 1.89,
        changePercent: 1.07,
        marketCap: '1.8T',
        volume: '35.2M',
        dayHigh: 179.80,
        dayLow: 176.90,
        history: generateDemoHistory(178.35)
    }
};

// Utility functions
function generateDemoHistory(basePrice) {
    const history = [];
    const days = 30;
    let price = basePrice;
    
    for (let i = days; i >= 0; i--) {
        const date = new Date();
        date.setDate(date.getDate() - i);
        
        // Add some random variation
        const change = (Math.random() - 0.5) * 10;
        price = Math.max(price + change, basePrice * 0.8);
        
        history.push({
            date: date.toISOString().split('T')[0],
            price: parseFloat(price.toFixed(2))
        });
    }
    
    return history;
}

function showLoading() {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('error').style.display = 'none';
    document.getElementById('stockInfo').style.display = 'none';
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    hideLoading();
}

function hideError() {
    document.getElementById('error').style.display = 'none';
}

// Stock data functions
async function searchStock() {
    const symbol = document.getElementById('stockSymbol').value.toUpperCase().trim();
    if (!symbol) {
        showError('Please enter a stock symbol');
        return;
    }
    
    loadStock(symbol);
}

async function loadStock(symbol) {
    currentSymbol = symbol;
    showLoading();
    hideError();
    
    // Simulate API delay
    setTimeout(() => {
        if (demoData[symbol]) {
            displayStockData(demoData[symbol]);
            renderChart(demoData[symbol].history);
            hideLoading();
        } else {
            showError(`Stock symbol "${symbol}" not found. Try popular stocks like AAPL, GOOGL, MSFT, TSLA, or AMZN.`);
        }
    }, 1000);
}

function displayStockData(data) {
    const stockInfo = document.getElementById('stockInfo');
    
    // Update header
    document.getElementById('stockName').textContent = `${data.name} (${data.symbol})`;
    document.getElementById('currentPrice').textContent = `$${data.price.toFixed(2)}`;
    
    const changeElement = document.getElementById('priceChange');
    const changeText = `${data.change >= 0 ? '+' : ''}${data.change.toFixed(2)} (${data.changePercent >= 0 ? '+' : ''}${data.changePercent.toFixed(2)}%)`;
    changeElement.textContent = changeText;
    changeElement.className = `price-change ${data.change >= 0 ? 'positive' : 'negative'}`;
    
    // Update details
    document.getElementById('marketCap').textContent = data.marketCap;
    document.getElementById('volume').textContent = data.volume;
    document.getElementById('dayHigh').textContent = `$${data.dayHigh.toFixed(2)}`;
    document.getElementById('dayLow').textContent = `$${data.dayLow.toFixed(2)}`;
    
    stockInfo.style.display = 'block';
    
    // Update watchlist button
    updateWatchlistButton();
}

function renderChart(history) {
    const ctx = document.getElementById('stockChart').getContext('2d');
    
    if (currentChart) {
        currentChart.destroy();
    }
    
    const labels = history.map(item => item.date);
    const prices = history.map(item => item.price);
    
    currentChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: `${currentSymbol} Price`,
                data: prices,
                borderColor: '#667eea',
                backgroundColor: 'rgba(102, 126, 234, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#667eea',
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
                pointRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    display: true,
                    grid: {
                        display: false
                    }
                },
                y: {
                    display: true,
                    grid: {
                        color: 'rgba(0,0,0,0.1)'
                    },
                    ticks: {
                        callback: function(value) {
                            return '$' + value.toFixed(2);
                        }
                    }
                }
            },
            interaction: {
                intersect: false,
                mode: 'index'
            }
        }
    });
}

function changeTimeframe(timeframe) {
    // Update active button
    document.querySelectorAll('.chart-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    // In a real app, this would fetch different data based on timeframe
    // For demo, we'll just show the same data
    if (currentSymbol && demoData[currentSymbol]) {
        renderChart(demoData[currentSymbol].history);
    }
}

// Watchlist functions
function updateWatchlistButton() {
    const watchlistBtn = document.querySelector('.watchlist-btn');
    if (watchlistBtn) {
        watchlistBtn.remove();
    }
    
    const isInWatchlist = watchlist.includes(currentSymbol);
    const btn = document.createElement('button');
    btn.className = 'watchlist-btn';
    btn.innerHTML = `<i class="fas fa-${isInWatchlist ? 'star' : 'star-o'}"></i> ${isInWatchlist ? 'Remove from' : 'Add to'} Watchlist`;
    btn.onclick = () => toggleWatchlist(currentSymbol);
    
    document.querySelector('.stock-header').appendChild(btn);
}

function toggleWatchlist(symbol) {
    const index = watchlist.indexOf(symbol);
    if (index > -1) {
        watchlist.splice(index, 1);
    } else {
        watchlist.push(symbol);
    }
    
    localStorage.setItem('stockWatchlist', JSON.stringify(watchlist));
    updateWatchlistButton();
    renderWatchlist();
}

function renderWatchlist() {
    const watchlistContainer = document.getElementById('watchlist');
    
    if (watchlist.length === 0) {
        watchlistContainer.innerHTML = '<p class="empty-watchlist">Add stocks to your watchlist to track them easily</p>';
        return;
    }
    
    watchlistContainer.innerHTML = watchlist.map(symbol => {
        const data = demoData[symbol];
        if (!data) return '';
        
        return `
            <div class="watchlist-item">
                <div>
                    <div class="symbol">${symbol}</div>
                    <div class="price">$${data.price.toFixed(2)}</div>
                </div>
                <div>
                    <div class="change ${data.change >= 0 ? 'positive' : 'negative'}">
                        ${data.change >= 0 ? '+' : ''}${data.change.toFixed(2)} (${data.changePercent >= 0 ? '+' : ''}${data.changePercent.toFixed(2)}%)
                    </div>
                    <button class="remove" onclick="toggleWatchlist('${symbol}')" title="Remove from watchlist">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
            </div>
        `;
    }).join('');
}

// Event listeners
document.getElementById('stockSymbol').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchStock();
    }
});

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    renderWatchlist();
    
    // Add some CSS for watchlist button
    const style = document.createElement('style');
    style.textContent = `
        .watchlist-btn {
            padding: 8px 16px;
            background: #ffd700;
            color: #333;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            margin-left: 20px;
            transition: all 0.3s;
        }
        
        .watchlist-btn:hover {
            background: #ffed4e;
            transform: translateY(-2px);
        }
    `;
    document.head.appendChild(style);
});
