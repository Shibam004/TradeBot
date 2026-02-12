from binance.enums import *

class OrderManager:
    def __init__(self, client_wrapper):
        self.client = client_wrapper.client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": float(quantity),
            }

            if order_type.upper() == "LIMIT":
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                params["price"] = str(price)
                params["timeInForce"] = "GTC"

            # API Call to Binance Futures Testnet
            response = self.client.futures_create_order(**params)
            return response
        except Exception as e:
            raise e