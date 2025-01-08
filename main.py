import requests
import datetime
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY = "5SZ2YJRWZCPWULIH"
NEWS_API = "6746c7c82b064f41b344894f301c0b6d"


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {"function": "TIME_SERIES_DAILY",
                    "symbol": STOCK,
                    "apikey": API_KEY}

url = 'https://www.alphavantage.co/query'
r = requests.get(url, params=stock_parameters)
data = r.json()['Time Series (Daily)']
past_data = [x for x in data.values()]

yesterdays_closing = float(past_data[0]["4. close"])
day_before_data = float(past_data[1]["4. close"])

per_chng= ((yesterdays_closing - day_before_data)/day_before_data)
# print(per_chng)

# print(yesterdays_closing,day_before_data)




news_parameter = {"apikey": NEWS_API,
                  "qInTitle": COMPANY_NAME,
                  "language": "en",
                  "sortBy": "popularity"}

res = requests.get("https://newsapi.org/v2/everything", params=news_parameter)
news_data = res.json()
news_list = []
for news in news_data["articles"][:3]:
    x = {"title": news['title'], "brief": news['description']}
    news_list.append(x)
    # print(f"{news['title']}\n{news['description']} \n\n\n")
print(news_list)

# Send a seperate message with the percentage change and each article's title and description to your phone number. 
if per_chng <=-5 or per_chng >= 5:
    for _ in news_list:
        # sms code twilio
        print(f"{_['title']}\n{_['brief']}\n\n")





# Determine the direction of the percentage change and format the message
direction = "🔺" if per_chng > 0 else "🔻"
formatted_per_chng = f"{direction}{abs(per_chng) * 100:.2f}%"

# Prepare and print the formatted message
for article in news_list:
    message = f"""
{STOCK}: {formatted_per_chng}
Headline: {article['title']}
Brief: {article['brief']}
"""
    print(message)