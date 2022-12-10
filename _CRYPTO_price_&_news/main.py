# check crypto portfolio price change, return this change and link some news regarding each cryptocurrency
from newsapi import NewsApiClient
import requests
import datetime as dt
import os
import smtplib

#############################################
#⚠️⚠️⚠️⚠️⚠️ DO NOT COPY KEYS ⚠️⚠️⚠️⚠️⚠️#
#############################################
os.environ["NEWS_API_KEY"] = "**********************"
os.environ["ALPHA_VANTAGE_API_KEY"] = "*********************"

#############################################
#                   IDEAS                   #
#############################################
# TODO: export APIs to separate file to load from
# TODO: insert data into csv, read CSV and return graph over time
# TODO: implement GUI to be able select grpah for selected period of time from: dd.mm.yyyy, to: dd.mm.yyyy (including)
# TODO: GET PRICE CHANGE - simplify

#############################################
#               MAIN VARIABLES              #
#############################################
ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

crypto = {
    "BTC": "bitcoin",
    "RUNE": "thorchain",
    "ADA": "cardano"
}

crypto_symbol = [key for (key, value) in crypto.items()]

#############################################
#               SETUP E-MAIL                #
#############################################


#############################################
#               GET PRICE CHANGE            #
############################################
# Get date
get_date = dt.datetime.now()
yesterday = get_date.day - 1
if yesterday < 10:
    yesterday = f"0{yesterday}"
month = get_date.month
if month < 10:
    month = f"0{month}"
year = get_date.year
yesterday_date = f"{year}-{month}-{yesterday}"

# Print changes
for symbol in crypto_symbol:
    # Get API data
    url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market=EUR&apikey={ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()
    # get open and close price within 24h
    yesterday_open = round(float(
        data["Time Series (Digital Currency Daily)"][yesterday_date]["1a. open (EUR)"]), 2)
    yesterday_close = round(float(
        data["Time Series (Digital Currency Daily)"][yesterday_date]["4a. close (EUR)"]), 2)
    # 5% change
    price_change = round(yesterday_open * 0.05, 2)
    change_in_percent = round((yesterday_close - yesterday_open) /
                              (yesterday_open * 0.01), 2)
    # return result
    if yesterday_open + (price_change) < yesterday_close:
        print(
            f"{symbol} price within 24h raised over🔺5% ({price_change} EUR) - new price was {yesterday_close} EUR({change_in_percent}%)\n")
    elif yesterday_open - (price_change) > yesterday_close:
        print(
            f"{symbol} price within 24h fall over🔻5% (-{price_change} EUR) - new price was {yesterday_close} EUR({change_in_percent}%)\n")
    else:
        print(
            f"{symbol} price change {change_in_percent}%. Today's starting price was {yesterday_close} EUR.\n")

#############################################
#                   GET NEWS                #
#############################################
# # setup source: CNN, reuters,
# # setup publishedAt: date
# # setup return source, title, description and link
news_page = "https://newsapi.org/v2/everything?"
parameters = {
    "q": "bitcoin",
    "apiKey": NEWS_API_KEY
}

request = requests.get(url=news_page, params=parameters)
data = request.json()["articles"][:3]
for i in range(0, len(data)):
    title = f'"{data[i]["source"]["name"]}": {data[i]["title"]}'
    desc = data[i]["description"]
    link = data[i]["url"]
    print(title)

# #############################################
# #                EXECUTE                    #
# #############################################
# when each part done, put together and run, check result
