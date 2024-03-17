import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

sb.set_style('whitegrid')
plt.style.use('fivethirtyeight')

from pandas_datareader.data import DataReader
import yfinance as yf
from pandas_datareader import data as pdr

yf.pd_override()

from datetime import datetime

tech_list = ['AAPL', 'GOOG', 'AMZN']
tech_list = ['AAPL', 'GOOG', 'AMZN']
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)

for stock in tech_list:
    globals()[stock] = yf.download(stock, start, end)

company_list = ['AAPL', 'GOOG', 'AMZN']
company_name = ['AAPLE', 'GOOGLE', 'AMAZON']

for company, com_name in zip(company_list, company_name):
    company["company_name"] = com_name

df = pd.concat(company_list, axis=0)
df.tail(10)
print(df.tail(10))

