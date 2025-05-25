# bot.py
import argparse

from utils import setup_logger

logger = setup_logger()


from binance.client import Client
from config import API_KEY, API_SECRET

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        
        print("✅ Connected to Binance Futures Testnet")
        logger.info("Connected to Binance Futures Testnet (Testnet mode: %s)", testnet)

    def get_futures_balance(self):
        try:
            balance = self.client.futures_account_balance()
            logger.info("Fetched futures account balance.")
            print("📊 Futures Account Balances:")
            for asset in balance:
                print(f"Asset: {asset['asset']}, Balance: {asset['balance']}, Available: {asset['availableBalance']}")
            logger.info("Balance details: %s", balance)
        except Exception as e:
            logger.error(f"Error fetching balance: {e}")
            print(f"❌ Error fetching balance: {e}")


    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )
            logger.info(f"Market order placed: {order}")
            print(f"✅ Market Order Placed: {order['symbol']} {order['side']} {order['origQty']} units")
            print(f"Status: {order['status']}, Order ID: {order['orderId']}")
        except Exception as e:
            logger.error(f"Market order error: {e}")
            print(f"❌ Error placing market order: {e}")


    
    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            logger.info(f"Limit order placed: {order}")
            print(f"✅ Limit Order Placed: {order['symbol']} {order['side']} {order['origQty']} @ {order['price']}")
            print(f"Status: {order['status']}, Order ID: {order['orderId']}")
        except Exception as e:
            logger.error(f"Limit order error: {e}")
            print(f"❌ Error placing limit order: {e}")


    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='STOP',
                quantity=quantity,
                price=limit_price,
                stopPrice=stop_price,
                timeInForce='GTC'
            )
            logger.info(f"Stop-limit order placed: {order}")
            print(f"✅ Stop-Limit Order Placed: {symbol} {side.upper()} @ Stop: {stop_price}, Limit: {limit_price}")
        except Exception as e:
            logger.error(f"Stop-limit order error: {e}")
            print(f"❌ Error placing stop-limit order: {e}")
    
    def get_open_positions(self):
        try:
            positions = self.client.futures_position_information()
            open_positions = [
                p for p in positions
                if float(p['positionAmt']) != 0
            ]
            return open_positions
        except Exception as e:
            logger.error(f"Error fetching open positions: {e}")
            return []



    
def parse_cli_args():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", type=str, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, choices=["buy", "sell"], help="Order side")
    parser.add_argument("--type", type=str, choices=["market", "limit", "stop-limit"], help="Order type")
    parser.add_argument("--qty", type=float, help="Quantity to trade")
    parser.add_argument("--price", type=str, help="Limit price (for limit or stop-limit)")
    parser.add_argument("--stop", type=str, help="Stop price (for stop-limit)")
    return parser.parse_args()






# Run test
if __name__ == "__main__":
    bot = BasicBot(API_KEY, API_SECRET)
    args = parse_cli_args()

    if args.symbol and args.side and args.type and args.qty:
        if args.type == "market":
            bot.place_market_order(args.symbol, args.side, args.qty)
        elif args.type == "limit" and args.price:
            bot.place_limit_order(args.symbol, args.side, args.qty, args.price)
        elif args.type == "stop-limit" and args.price and args.stop:
            bot.place_stop_limit_order(args.symbol, args.side, args.qty, args.stop, args.price)
        else:
            print("❌ Missing price or stop price for limit/stop-limit order.")
    else:
        print("❌ Missing required CLI arguments. Use --help for usage.")


