from robobrowser import RoboBrowser
import re
from bs4 import BeautifulSoup
import json



def GetWeather():

 browser = RoboBrowser(parser="html.parser")

 browser.open("https://weather.com/ru-BY/weather/today/l/c855859306f030f8d49f5384679a817861c690451a73f3d35ca55ec197aa452a")

 weather_today = browser.select(".Column--column--1p659")

 weather_dict = {}

 key_num = 0

 for x in weather_today[:4]:

     soup = BeautifulSoup(f"{x}",'html.parser')

     span_list = soup.find_all('span')

     span_data = [span.get_text() for span in span_list]

     title_list = soup.find_all('title')

     title_data = [title.get_text() for title in title_list]

     #print(f"vse elementy span {span_data} and title {title_data}")

     concatted = span_data[:3] + title_data

     weather_dict[key_num] = concatted

     key_num += 1




 return weather_dict




