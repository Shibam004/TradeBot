import streamlit as st
import os
from dotenv import load_dotenv
from bot.client import BinanceTestnetClient
from bot.orders import OrderManager
from bot.logging_config import setup_logging

load_dotenv()
logger = setup_logging()

# Page Styling
st.set_page_config(page_title="Binance Bot Pro", layout="centered")
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #f0b90b; color: black; font-weight: bold; }
    .stTextInput>div>div>input { color: #f0b90b; }
    </style>
    """, unsafe_allow_html=True)

st.title("🟡 TradeBot")
st.divider()

# Credentials Handling
with st.sidebar:
    st.header("🔐 Credentials")
    env_key = os.getenv('BINANCE_API_KEY')
    if env_key:
        st.success("API Key loaded from .env")
        api_key = env_key
        api_secret = os.getenv('BINANCE_API_SECRET')
    else:
        st.warning("No .env found. Enter manually:")
        api_key = st.text_input("API Key", type="password")
        api_secret = st.text_input("API Secret", type="password")

# Order Form
with st.container(border=True):
    st.subheader("🚀 Quick Trade")
    c1, c2 = st.columns(2)
    
    with c1:
        symbol = st.text_input("Symbol", value="BTCUSDT").upper()
        side = st.radio("Side", ["BUY", "SELL"], horizontal=True)
    
    with c2:
        order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
        quantity = st.number_input("Quantity", min_value=0.001, step=0.001, format="%.3f")

    price = None
    if order_type == "LIMIT":
        price = st.number_input("Limit Price", min_value=1.0)

    if st.button("EXECUTE ORDER"):
        try:
            bot_client = BinanceTestnetClient(api_key, api_secret)
            manager = OrderManager(bot_client)
            
            with st.status("Communicating with Binance...", expanded=True) as status:
                st.write("Validating inputs...")
                result = manager.place_order(symbol, side, order_type, quantity, price)
                status.update(label="Order Executed Successfully!", state="complete", expanded=False)
            
            st.balloons()
            st.json(result)
            logger.info(f"UI Order Success: {result.get('orderId')}")
            
        except Exception as e:
            st.error(f"❌ Execution Failed: {str(e)}")
            logger.error(f"UI Order Error: {str(e)}")