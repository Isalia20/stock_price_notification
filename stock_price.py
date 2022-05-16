import os
import sys

import yfinance as yf
from apscheduler.schedulers.blocking import BlockingScheduler

CURRENT_DIR = os.path.dirname(os.path.abspath("C:\\Users\\Irakli Salia\\OneDrive\\IRAKLI\\stock_price_notification\\stock_price_notification\\utils\\stock_notif_class.py"))
sys.path.append(os.path.dirname(CURRENT_DIR))
from utils import stock_notif_class

tickers = ["AAPL", "NVDA", "MSFT", "VORB", "TSLA", "EPAM"]
price_dict = {}

for ticker in tickers:
    price_dict[ticker + str("_yesterday")] = yf.Ticker(ticker).history(period='2d', interval='1d', actions=False)\
                                                    .iloc[0]["Close"]


def some_job():
    spn = stock_notif_class.StockPriceNotification(email="mail", password="pass")
    for ticker in tickers:
        price_dict[ticker + str("_today")] = spn.get_stock_price(ticker)
        # Calculate decrease percentage
        price_today = price_dict[ticker + str("_today")]
        price_yesterday = price_dict[ticker + str("_yesterday")]
        diff = round(abs((price_today - price_yesterday) / price_yesterday),2)
        diff *= 100
        if diff >= 4:
            spn.send_mail(ticker, diff)


scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', hours=1/6, max_instances=5)
scheduler.start()
