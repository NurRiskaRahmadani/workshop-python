from bs4 import BeautifulSoup
import requests

url = "https://www.kaggle.com/datasets/iganarendra/zoom-fatigue-pada-mahasiswa-indonesia/ZoomFatigue.csv"

web = requests.get(url).text
s = BeautifulSoup(web, "csv")
b = s.find('div', attrs={'class':'sc-dhyxXW'})
print("Zoom Fatigue pada Mahasiswa Indonesia")
