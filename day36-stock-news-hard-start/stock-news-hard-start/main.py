import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = 'b2187595b4a6474b9aadc0532b558c84'

STOCK_API = 'NKWZXWA2PPW6OBXM'

parameters = {
    'q':COMPANY_NAME,
    'apiKey':API_KEY
}

stock_parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':STOCK_API
}
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



response_stock = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response_stock.raise_for_status()
stock_prices = response_stock.json()['Time Series (Daily)']

sorted_dates = sorted(stock_prices.keys(), reverse=True)
latest_date = sorted_dates[0]
previous_date = sorted_dates[1]

latest_close = float(stock_prices[latest_date]['4. close'])
previous_close = float(stock_prices[previous_date]['4. close'])

diffrence = abs(latest_close - previous_close)
diff_percent = (diffrence/latest_close) * 100

if diff_percent > 5:
    res = requests.get(NEWS_ENDPOINT, params=parameters)
    res.raise_for_status()
    articles = res.json()['articles'][:2]
    print(articles)



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

