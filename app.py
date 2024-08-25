from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app)

@app.route('/api/spy-price', methods=['GET'])
def get_spy_price():
    try:
        # Fetch SPY data from Yahoo Finance
        spy = yf.Ticker("SPY")
        # Get the latest market data
        spy_price = spy.history(period="1d")['Close'].iloc[-1]
        
        return jsonify({'price': round(spy_price, 2)})
    
    except Exception as e:
        app.logger.error(f"Error fetching price: {e}")
        return jsonify({'error': 'Failed to fetch price'}), 500

if __name__ == '__main__':
    app.run(debug=True)
