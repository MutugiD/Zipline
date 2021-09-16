import talib 
import yfinance as yf  
import numpy as np
import pandas as pd


def download_data(sign=None, start=None, interval=None, end=None):
  data = yf.download(sign, start=start, interval=interval,  end=end ,progress=False)
  return data
    
#tickers = ["BCH-USD",  "BTC-USD", "DOGE-USD", "ETH-USD", "THETA-USD", "MATIC-USD", "VET-USD", "XRP-USD"] 

BCH = yf.download("BCH-USD", start='2018-01-01', interval='1d',  end='2021-08-24') 
BCH.csv('data/bars_adj/BSH.csv')