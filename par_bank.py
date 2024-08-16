import requests
from bs4 import BeautifulSoup
import csv
import time

# URL для отзывов
url = "https://www.banki.ru/services/responses/list"


respons = requests.get(url)



# print(10)