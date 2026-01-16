"""
Docstring for cards.get_cards
"""

import os
import requests


def download_image(img_name: str, url: str, path: str) -> str:
    """
    Docstring for download_image

    :param img_name: Description
    :type img_name: str
    :param url: Description
    :type url: str
    :param path: Description
    :type path: str
    """
    img_data = requests.get(url, timeout=60).content
    with open(os.path.join(path, img_name + '.png'), 'wb') as handler:
        handler.write(img_data)

        print(f'{img_name} saved!')


os.makedirs('cards/images', exist_ok=True)

URL = 'http://api.magicthegathering.io/v1/cards'
params = {'page': 0}
MAX_PAGE = 937
COUNT = 0

while params['page'] <= MAX_PAGE:
    print(params['page'])

    response = requests.get(URL, params=params, timeout=60)
    params['page'] += 1

    if response.status_code == 200:
        data = response.json()

        print(len(data['cards']))

        for card in data['cards']:
            name = card['name']
            image = card.get('imageUrl')

            name = name + f'_{COUNT}'

            if not image:
                continue

            download_image(path='cards/images', img_name=name, url=image)

            COUNT += 1
