import argparse
from bot.client import BinanceTestnetClient
from bot.orders import OrderManager
from bot.logging_config import setup_logging

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures CLI Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True)
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--key", required=True)
    parser.add_argument("--secret", required=True)

    args = parser.parse_args()

    try:
        bot_client = BinanceTestnetClient(args.key, args.secret)
        manager = OrderManager(bot_client)
        result = manager.place_order(args.symbol, args.side, args.type, args.qty, args.price)
        print(f"Success! Order ID: {result.get('orderId')}")
        logger.info(f"CLI Success: {result.get('orderId')}")
    except Exception as e:
        print(f"Error: {e}")
        logger.error(f"CLI Error: {str(e)}")

if __name__ == "__main__":
    main()