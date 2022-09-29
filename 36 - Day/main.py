from twilio.rest import Client
import requests
import math


account_sid = "AC12407e5ef62b6460df405419a923da86"
auth_token = "a895ea36b6c70e3263152173435dbd0f"
client = Client(account_sid, auth_token)

AV_API = "MVGGD6AGC49LE78K"
NEW_API = "9d79fdb36a564fa893c346aedecdd5a1"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API,
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEW_API
}


#   STOCK PRICE
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
today = stock_data["2022-09-27"]["4. close"]
yesterday = stock_data["2022-09-26"]["4. close"]
compare = math.ceil(float(today) - float(yesterday))

result = None
if compare > 0:
    result = f"{STOCK} ⬆ {compare}"
else:
    result = f"{STOCK} ⬇ {compare}"


#   NEWS
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()

news_data = news_response.json()
article = news_data["articles"][0]
headline = article["title"]
brief = article["content"]


#   SMS
final_message = f"{result}\nHeadline: {headline}\nBrief: {brief}"

message = client.messages.create(
                     body=final_message,
                     from_="+12058434651",
                     to="+918971818410"
                 )

print(message.status)



# STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.


# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

