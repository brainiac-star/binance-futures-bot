# 🔁 Binance Futures Trading Bot (Testnet)

A Python-powered trading bot built for the Binance USDT-M Futures **Testnet**.  
Supports **Market, Limit, and Stop-Limit orders** via both **command-line interface** and a **Streamlit web UI**.

---

## ⚙️ Features

- ✅ Place Market, Limit, and Stop-Limit Orders
- ✅ User-friendly Streamlit Web Interface
- ✅ Command-line Interface with `argparse`
- ✅ Real-time Open Position Viewer
- ✅ Full logging of API activity and errors
- ✅ Modular and extensible Python structure

---

## 📂 Project Structure

```
trading_bot/
├── bot.py         # Core trading logic (market, limit, stop-limit)
├── config.py      # Binance API credentials (excluded from Git)
├── ui.py          # Streamlit app for placing/viewing orders
├── utils.py       # Logger setup
├── logs/
│   └── bot.log    # All logs (API + error)
├── requirements.txt
└── README.md
```

---

## 🔐 Setup Instructions

### 1. Clone and Navigate
```bash
git clone https://github.com/brainiac-star/binance-futures-bot.git
cd binance-futures-bot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate       # Windows
# or
source venv/bin/activate    # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Binance API Setup

1. Register on [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Create your API key and secret
3. Create `config.py` in the root:
```python
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
```

---

## 🚀 Usage

### 📌 1. CLI Mode
```bash
# Market Buy
python bot.py --symbol BTCUSDT --side buy --type market --qty 0.001

# Limit Sell
python bot.py --symbol BTCUSDT --side sell --type limit --qty 0.002 --price 75000

# Stop-Limit Sell
python bot.py --symbol BTCUSDT --side sell --type stop-limit --qty 0.002 --stop 67000 --price 68000
```

### 🖥️ 2. Streamlit Web UI
```bash
streamlit run ui.py
```

- Input fields for symbol, side, order type, quantity, price
- One-click submission
- Live position viewer below

---

## 💻 Sample Outputs

### ✅ Terminal Output (CLI)
```
✅ Market Order Placed: BTCUSDT BUY 0.001 units
Status: NEW, Order ID: 4459791561
✅ Limit Order Placed: BTCUSDT SELL 0.002 @ 75000.00
Status: NEW, Order ID: 4459791837
✅ Stop-Limit Order Placed: BTCUSDT SELL @ Stop: 67000, Limit: 68000
```

### 📊 Sample Logs (`logs/bot.log`)
```
2025-05-25 20:28:57 - INFO - Connected to Binance Futures Testnet
2025-05-25 20:29:18 - INFO - Market order placed: {'symbol': 'BTCUSDT', 'side': 'BUY', ...}
```

### 🌐 UI Screenshot 

![image](https://github.com/user-attachments/assets/7e1fb8e5-acee-4a49-bab1-6c398a12e19a)
![image](https://github.com/user-attachments/assets/a00eb945-561f-4c07-8079-70164604d5a5)


---

