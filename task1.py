# 1. Отримати курси евро за попередній тиждень, вивести на екран дату + курс
# 2. З отриманого словника побудувати графк зміни курсу за тиждень
# URL for request https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250317&end=20250321&valcode=eur&json
import json
import requests

nbu_response = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250301&end=20250328&valcode=eur&json")


converted_response = json.loads(nbu_response.content)

for item in converted_response:
    #Go through a loop here

# Matplotlib

import matplotlib.pyplot as plt


