import requests
import json
from bs4 import BeautifulSoup


string = requests.get("https://jikan.me/api/anime/1")



soup = BeautifulSoup(string.text, 'html.parser')

x = soup.find("image")
print(x)






