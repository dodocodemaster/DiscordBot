import requests
from tokens import deepai_token


def create_img(mess):


    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': mess,
        },
        headers={'api-key': deepai_token.KEY}
    )
    URL = r.json().get('output_url')
    if URL == None:
        return 'deep_img/error.jpg'
    print(URL)
    r = requests.get(URL)
    if r.status_code == 200:
        with open('deep_img/dimg.jpg', 'wb') as imgfile:
            imgfile.write(r.content)
        return 'deep_img/dimg.jpg'