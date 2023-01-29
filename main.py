import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "cd74dba04abd4f098e89d2417ee7c59c"
STOCK_API_KEY = "AMGOWU3MUEBYFY4S"

# Parameters for stock endpoint request:
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]
yeserday_data = data_list[0]
yesterday_closing_price = yeserday_data["4. close"]
print(yesterday_closing_price)
