# 1. Отримати курси евро за попередній тиждень, вивести на екран дату + курс
# 2. З отриманого словника побудувати графк зміни курсу за тиждень
import json
import requests

# URL for request https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250317&end=20250321&valcode=eur&json
response_data = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250317&end=20250321&valcode=eur&json")

response_list = json.loads(response_data.content)

exchange_date = []
exchange_rate = []
# Logic to extract data from NBU service response


### Part 2
# Matplotlib
# import matplotlib.pyplot as plt
#
# plt.plot(exchange_date, exchange_rate)
# plt.show()





