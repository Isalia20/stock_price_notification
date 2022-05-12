from stock_price_notification.utils import stock_functions

valid_tickers = [""]

spn = stock_functions.StockPriceNotification(ticker= "MSFT", email = "mail_1",password="pass")

def some_job():
    get_stock_price()

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', hours=1)
scheduler.start()
