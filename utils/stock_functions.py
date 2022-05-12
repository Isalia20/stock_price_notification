import yfinance as yf
import yagmail


class StockPriceNotification:
    def __init__(self,
                 ticker,
                 email,
                 password):
        self.ticker = ticker
        self.email = "mail"
        self.password = "pass"
        self.stock_price = self.get_stock_price()

    # Functions used in stock price file and for general notifications
    def get_stock_price(self):
        return yf.Ticker(self.ticker).get_info()["regularMarketPrice"]

    def _initialize_receivers(self):
        mail_message = {
            "mail_1": [f"Price for {self.ticker} is {self.stock_price}",
                                          "Your dear scheduled script"],
            "mail_2": [f"Price for {self.ticker} is {self.stock_price}",
                                   "Tell Irakli about this mail"]
        }
        return mail_message

    def _initialize_mail_client(self):
        yag = yagmail.SMTP(self.email, self.password)
        return yag

    def send_mail(self):
        mail_message = self._initialize_receivers()
        yag = self._initialize_mail_client()
        for i in mail_message.keys():
            yag.send(i, mail_message[i][0], mail_message[i][1])
        print("Done Sending")
