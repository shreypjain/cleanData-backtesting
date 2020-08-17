import yfinance as yf
import back_testing
import pandas as pd
import requests as rq
from config import get_access_token, get_refresh_token,get_consumer_key
import mysql.connector

class BackTesting():
    def main(self):
        return "nothing yet"
    def load_data():
        df = pd.read_csv("tickersS&P.csv")
        for i in df['Symbol']:
            req = rq.get("https://api.tdameritrade.com/v1/marketdata/" +i+"/pricehistory",{
                "apikey":get_consumer_key()
            })
            print(req.text)
    def parse_data():
        payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        df = payload[0]
        df.to_csv('tickersS&P.csv',columns=['Symbol'])

    def cleanse_data(self):
        print("cleansing data")

BackTesting.load_data()