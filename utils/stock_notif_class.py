import yfinance as yf
import yagmail


class StockPriceNotification:
    def __init__(self,
                 email,
                 password):
        self.email = email
        self.password = password

    # Functions used in stock price file and for general notifications
    @staticmethod
    def get_stock_price(ticker):
        return yf.Ticker(ticker).get_info()["regularMarketPrice"]

    @staticmethod
    def _initialize_receivers():
        mail_message = {
            "irakli.salia854@gmail.com": ["ticker is down percentage_down %",
                                          "Your dear scheduled script"],
            "elizkhel@gmail.com": ["ticker is down percentage_down %",  # ticker and percentage_down get replaced below
                                   "Tell Irakli about this mail"]
        }
        return mail_message

    def _initialize_mail_client(self):
        yag = yagmail.SMTP(self.email, self.password)
        return yag

    def send_mail(self, ticker, percentage_fall):
        mail_message = self._initialize_receivers()
        yag = self._initialize_mail_client()
        # stock_price = self.get_stock_price(ticker)
        for i in mail_message.keys():
            subject = mail_message[i][0].replace("ticker", str(ticker))
            subject = subject.replace("percentage_down", str(percentage_fall))
            body = mail_message[i][1]
            yag.send(i, subject, body)
        print("Done Sending")
