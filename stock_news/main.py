STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
import requests
import json
import os
from twilio.rest import Client

ALPHA_API_KEY = "DSJH536EL93QL9UD"
NEWS_API_KEY = "5c934a5ba69f4afd93556418e20db6ec"
TWILIO_NUMBER = "+12183323260"
alpha_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"
# https://newsapi.org/v2/everything?q=tesla&from=2022-12-17&sortBy=publishedAt&apiKey=5c934a5ba69f4afd93556418e20db6ec


alpha_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize" : "full",
    "apikey" : ALPHA_API_KEY
}
alpha_response = requests.get(url=alpha_url, params=alpha_params)
data = alpha_response.json()
data["Time Series (Daily)"]['2023-01-13']
# with open("/home/beast/100Days/stock_news/results.json", "w") as f:
#     json.dump(data, f)
today_data = float(data["Time Series (Daily)"][list(data["Time Series (Daily)"].keys())[0]]["4. close"])
yesterday_data = float(data["Time Series (Daily)"][list(data["Time Series (Daily)"].keys())[1]]["4. close"])
yesterday_data = 110
difference = (today_data - yesterday_data) / today_data * 100
if difference > 5 :
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_params = {
    "q":COMPANY_NAME,
    "from": list(data["Time Series (Daily)"].keys())[1],
    "sortBy":'published',
    "apiKey": NEWS_API_KEY
    }   
    news_response = requests.get(url=news_url, params=news_params)
    news_data = news_response.json()
    with open("/home/beast/100Days/stock_news/results.json", "w") as f:
        json.dump(news_data, f)
    news_selected = news_data["articles"][:3]
    news = {}
    for i in range(len(news_selected)):
        news.update({i : {"title" : news_selected[i]["title"] , "description" : news_selected[i]["description"]}})

    print(news)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    # Download the helper library from https://www.twilio.com/docs/python/install
    


    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message_text = ""
    for i in range(len(news)):
        message_text = f'{STOCK} up {str(difference)}%\nHeadline: {news[i]["title"]}\nBrief: {news[i]["description"]}\n'
        message = client.messages \
            .create(
                body=message_text,
                from_=TWILIO_NUMBER,
                to=os.environ['PHONE_NUMBER']
            )
        print(message.status)

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

