import pandas as pd
import yfinance as yf
from utils import stock_functions
from apscheduler.schedulers.blocking import BlockingScheduler

ticker = "MSFT"


#
# price_history_tick = yf.Ticker(ticker).history(period='2d',  # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
#                                    interval='1d',  # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
#                                    actions=False)
# price_history_tick = pd.DataFrame(price_history_tick)
#
# price_history_tick.iloc[0]

def some_job():
    spn = stock_functions.StockPriceNotification(email="mail", password="pass")
    spn.send_mail("MSFT")


scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', hours=1 / 60, max_instances=5)
scheduler.start()
