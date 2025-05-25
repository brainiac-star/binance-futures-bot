# ui.py

import streamlit as st
from bot import BasicBot
from config import API_KEY, API_SECRET

st.set_page_config(page_title="Binance Futures Bot", layout="centered")
st.title("📈 Binance Futures Trading Bot (Testnet)")

# Initialize bot
bot = BasicBot(API_KEY, API_SECRET)

# User input
symbol = st.text_input("Symbol", "BTCUSDT").upper()
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP-LIMIT"])

quantity = st.number_input("Quantity", min_value=0.001, step=0.001, format="%.3f")

price = None
stop_price = None

# Collect price inputs if needed
if order_type in ["LIMIT", "STOP-LIMIT"]:
    price_input = st.text_input("Limit Price")
    try:
        price = round(float(price_input), 2)
    except:
        price = None

if order_type == "STOP-LIMIT":
    stop_input = st.text_input("Stop Price")
    try:
        stop_price = round(float(stop_input), 2)
    except:
        stop_price = None

# Button to place order
if st.button("📤 Place Order"):
    if order_type == "MARKET":
        bot.place_market_order(symbol, side, quantity)
    elif order_type == "LIMIT":
        if price:
            bot.place_limit_order(symbol, side, quantity, price)
        else:
            st.error("⚠️ Please enter a valid limit price.")
    elif order_type == "STOP-LIMIT":
        if price and stop_price:
            bot.place_stop_limit_order(symbol, side, quantity, stop_price, price)
        else:
            st.error("⚠️ Please enter both stop and limit prices.")

st.subheader("📊 Open Positions")

positions = bot.get_open_positions()

if positions:
    for pos in positions:
        st.write(f"**Symbol:** {pos['symbol']}")
        st.write(f"- Position Amt: {pos['positionAmt']}")
        st.write(f"- Entry Price: {pos['entryPrice']}")
        st.write(f"- Mark Price: {pos['markPrice']}")
        st.write(f"- Unrealized PnL: {pos.get('unrealizedProfit', 'N/A')}")
        st.markdown("---")
else:
    st.info("No open positions.")

