# Binance Trading Bot 🤖

A modular and robust Python application designed to interact with the **Binance Futures Testnet (USDT-M)**[cite: 4, 10]. [cite_start]This project was developed as part of a Python Developer Intern assignment to demonstrate clean code architecture, error handling, and dual-interface accessibility.

## 🚀 Features
* **Order Placement**: Supports both `MARKET` and `LIMIT` orders.
* **Dual Side Support**: Execute both `BUY` and `SELL` operations.
* **Web UI**: Built with Streamlit for a colorful, user-friendly trading experience.
* **CLI Access**: Fully functional command-line interface for rapid order execution.
* **Automatic Logging**: Every request, response, and error is captured in `trading.log`.
* **Security**: Integration with `.env` files to protect sensitive API credentials.

## 📁 Project Structure
```text
trading_bot/
├── bot/
    ├── __init__.py
    ├── client.py          # Binance API wrapper & authentication
    ├── orders.py          # Core order placement logic 
    ├── logging_config.py  # Structured logging setup 
├── .env                  # Private credentials (not included in git)
├── .gitignore            # Security configuration
├── cli.py                 # CLI entry point 
├── gui.py                 # Streamlit Web UI entry point 
├── requirements.txt       # Project dependencies 
├── README.md              # Documentation
└── trading.log            # Activity logs
```

## 🛠️ Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/Shibam004/TradeBot.git](https://github.com/Shibam004/TradeBot.git)
   cd TradeBot
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Environment**: Create a `.env` file in the root directory and add your Binance Futures Testnet credentials:
   ```text
   BINANCE_API_KEY=your_testnet_key
   BINANCE_API_SECRET=your_testnet_secret
   ```
## 💻 How to Use
**Option 1: Web Interface (Streamlit):**
Launch the interactive dashboard:
```bash
streamlit run gui.py
```
**Option 2: Command Line Interface (CLI):**
Execute orders directly from your terminal:
```bash
# Example MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002 --key YOUR_KEY --secret YOUR_SECRET

# Example LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.002 --price 65000 --key YOUR_KEY --secret YOUR_SECRET
```

## 📝 Assumptions & Constraints
* **Environment**: Hardcoded to use the Binance Futures Testnet URL: `https://testnet.binancefuture.com`.
* **Asset Class**: Specifically designed for USDT-M (USDT-Margined) Futures.
* **Minimum Notional**: Orders must meet the exchange's minimum notional value (typically >$100 on testnet).
* **Precision**: Trading quantities for BTCUSDT are limited to the asset's specific step size (e.g., 0.001).
* **Time In Force**: LIMIT orders default to GTC (Good 'Til Cancelled).

## 📊 Evaluation Deliverables
This repository includes a trading.log file containing successful execution data for:
1. One **Market** Order
2. One **Limit** Order

## ✉️ Contact
For any queries regarding this submission, please contact:
* **Developer**: Shibam Karmakar
* **GitHub**: [Shibam Karmakar](https://github.com/Shibam004)
* **LinkedIn**: [Shibam Karmakar](https://www.linkedin.com/in/shibam-karmakar-b09423271/)
* **Mail**: [Mail me](shibamkarmakar809@gmail.com)
