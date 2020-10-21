import requests
from bs4 import BeautifulSoup as bs


def LNA(nickname):
    url = 'https://stats.onligamez.ru/?u='+ nickname +'&s=oz-bnet&st=10&lang=RU'


    response = requests.get(url)
    try:
        soup = bs(response._content , "lxml")
        stat = soup.find('div', attrs={'class': 'panel-body'})
        games = stat.find_all('b', attrs={'class': 'text-success'})

        pts = str(games[0].next)
        games_value = str(games[1].next)
        win = str(games[2].next)
        lose = str(games[3].next)
        wr = str(games[6].next)
    except Exception:
        return 'Игрок '+nickname+' не найден!'

    result ='⚔️PTS: '+ pts + '\n🕹️К-во игр: ' + games_value + '\n🛡Побед: ' + win + '\n☠Поражений: ' + lose + '\n♥️WinRate: ' + wr +  "%"
    
    return result
