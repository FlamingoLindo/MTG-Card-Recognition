"""
Docstring for cards.get_cards
"""

import re
import time
import os
import json
import requests


def sanitize_filename(filename: str) -> str:
    """
    Docstring for sanitize_filename

    :param file_name: Description
    :type file_name: str
    :return: Description
    :rtype: str
    """

    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    filename = filename.strip('. ')
    return filename


def download_image(img_name: str, url: str, path: str):
    """
    Docstring for download_image

    :param img_name: Description
    :type img_name: str
    :param url: Description
    :type url: str
    :param path: Description
    :type path: str
    """

    safe_name = sanitize_filename(img_name)

    img_data = requests.get(url, timeout=60).content
    with open(os.path.join(path, safe_name + '.png'), 'wb') as handler:
        handler.write(img_data)

        print(f'{img_name} saved!')


os.makedirs('cards/images', exist_ok=True)

URL = 'http://api.magicthegathering.io/v1/cards'
params = {'page': 0}
# 937
MAX_PAGE = 937
COUNT = 0
all_cards = []

while params['page'] <= MAX_PAGE:
    try:
        print('\033[1m\033[0;32mGetting cards from page: ',
              params['page'], '\033[0m')

        response = requests.get(URL, params=params, timeout=60)

        # Wait 5 minutes incase of any rate limits issues
        if response.status_code == 403:
            print(
                '\033[1m\033[0;31mRate limit exceeded. Waiting 5 minutes...\033[0m')
            time.sleep(300)
            continue

        if response.status_code == 200:
            data = response.json()

            # Will also count card that dont have "imgUrl",
            # so the script will probably save less then this
            print('\033[1m\033[0;34mCards in this page: ',
                  len(data['cards']), '\033[0m')

            for card in data['cards']:
                name = card['name']
                image = card.get('imageUrl')

                if not image:
                    continue

                new_name = name + f'_{COUNT}'

                download_image(path='cards/images',
                               img_name=new_name, url=image)

                all_cards.append(
                    {'id': COUNT, 'img': name, 'url': image, 'page': params['page']})

                COUNT += 1

    except (requests.RequestException, json.JSONDecodeError, OSError, KeyError, ValueError) as e:
        print(f"Error on page {params['page']}: {e}")
        all_cards.append({'error': str(e), 'page': params['page']})

    finally:
        params['page'] += 1

with open('cards/cards.json', 'w', encoding='utf-8') as f:
    json.dump(all_cards, f, ensure_ascii=False, indent=4)
