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
day_before_yesterday_data = data_list[1]
yesterday_closing_price = yeserday_data["4. close"]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
stock_price_difference = abs(float(yesterday_closing_price) -
                             float(day_before_yesterday_closing_price))
difference_percent = stock_price_difference / \
    float(yesterday_closing_price) * 100

# If stock price difference is more than specified int, get latest stock news:
if difference_percent > 5:
    # Parameters for news endpoint request:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": STOCK,
        "searchIn": "title"
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    top_articles = news_response.json()["articles"][:3]

formatted_articles = [
    f"Headline: {article['title']} \nBrief: {article['description']}" for article in top_articles]
