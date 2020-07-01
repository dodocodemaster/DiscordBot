import requests


def weather_status(search_city):
    search_city = search_city.replace(" ", "+")
    search_string = 'http://wttr.in/~' + search_city + '?format=j1'
    rs = requests.get(search_string)
    data = rs.json()

    return data


search_city = 'Сыктывкар'

data_w = weather_status(search_city)

print(data_w)
