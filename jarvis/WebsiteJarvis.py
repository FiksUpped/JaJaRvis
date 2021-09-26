import re
from bs4 import BeautifulSoup
import json
from robobrowser import RoboBrowser
from requests_html import HTMLSession

session = HTMLSession()



browser = RoboBrowser(parser="html.parser")


def GetWeather():



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











def GetNews():

  browser.open("https://ria.ru/world/")


  news_dict = {}

  lates_world_news = browser.select(".list-item__title")

  news_num = 0

  for news in lates_world_news:


      soup_news = BeautifulSoup(f"{news}", 'html.parser')

      news_list = soup_news.find_all('a')

      news_parsed = [news_list.get_text() for news_list in news_list]



      news_dict[news_num] = news_parsed

      news_num += 1


  return news_dict







def GetConcertList():

    browser.open("https://bandsintown.com/")

   # concert_dict = {}

   # upcoming_concerts = browser.select("._1IERtiskeoZuOUU03hZvgB")

    print(browser.parsed)

#GetConcertList()


def CinemaList():


    get_cinema_html = session.get("https://silverscreen.by/afisha/")

    get_cinema_html.html.render() #rendering javascript on page

    search_for_cinema_name = get_cinema_html.html.find('.sc-gnDgBH')

    parsed_list = [name_.text for name_ in search_for_cinema_name]

    return parsed_list


'''
    cinema_num = 0

    cinema_dict = {}

    browser.open("https://silverscreen.by/afisha/")

    print(browser.parsed())

    cinema_divs = browser.select(".sc-gnDgBH")

    for it in cinema_divs:

        soup_cinemas = BeautifulSoup(f"{it}", 'html.parser')

        cinema_list = soup_news.find_all('a')

        cinema_parsed = [cinema_list.get_text() for news_list in cinema_list]

        cinema_dict[news_num] = cinema_parsed

        cinema_num += 1

    print(cinema_dict)



'''

