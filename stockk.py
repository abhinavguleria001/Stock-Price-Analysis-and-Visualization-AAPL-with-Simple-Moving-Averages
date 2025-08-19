import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import yfinance as yf
stock = "AAPL"
data = yf.download(stock,start = "2020-01-01", end = "2025-01-01")
print(data.head())