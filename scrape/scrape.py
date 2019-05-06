import requests, urllib.request, time
from bs4 import BeautifulSoup

url = 'https://www.bovada.lv/sports/basketball/nba-playoffs/'
game = 'portland-trail-blazers-denver-nuggets-201905012105'
url = url + game
#

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
soup.findAll('a')
