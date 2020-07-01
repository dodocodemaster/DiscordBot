import requests
from bs4 import BeautifulSoup as bs


def LNA(nickname):
    url = 'https://stats.onligamez.ru/?u='+ nickname +'&s=wc3.theabyss.ru&st=10&lang=RU'


    response = requests.get(url)

    soup = bs(response._content , "lxml")
    stat = soup.find('div', attrs={'class': 'panel-body'})
    games = stat.find_all('b', attrs={'class': 'text-success'})

    pts = str(games[0].next) 
    games_value = str(games[1].next)
    win = str(games[2].next)
    lose = str(games[3].next)
    wr = str(games[6].next)


    result ='⚔️PTS: '+ pts + '\n🕹️К-во игр: ' + games_value + '\n🛡Побед: ' + win +  "%"+ '\n☠Поражений: ' + lose + '\n♥️WinRate: ' + wr
    
    return result
