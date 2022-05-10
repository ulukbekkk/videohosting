import requests
from bs4 import BeautifulSoup

url = 'https://www.kinonews.ru/news/'
images_url = 'https://www.kinonews.ru'

def get_soup(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    return soup


def get_all_news_title():
    soup = get_soup(url)
    block = soup.find('div', "block-main").find_all('div', "anons-title-new")
    title = [ x.text for x in block]
    return title


def get_all_news_body():
    soup = get_soup(url)
    block = soup.find_all('div', 'anons-text')
    body = [y.text.replace('\n', '').replace('\r', '') for y in block]
    return body


def get_all_news_images():
    soup = get_soup(url)
    block = soup.find_all('img', attrs={"class":"newsimg"})
    first_images = [ images_url + z.get('src') for z in block]
    return first_images

title = get_all_news_title()
body = get_all_news_body()
img = get_all_news_images()

zipped = list(zip(title, body, img))
print(zipped)

dict_parsing = {}
count = 1
# for a in range(0, len(title)):
#     dict_parsing[count] = list(title[a], body[a], img
#
#
# for m in dict_parsing.values():
#     print(m)

# a, b, c = dict_parsing.values()
#
# print( a,b,c)

