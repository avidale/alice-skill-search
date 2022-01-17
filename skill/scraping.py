import time

import requests


def collect_docs():
    all_items = []
    for i in range(1, 100):
        n = 6
        for attempt in range(n):
            try:
                r = requests.get('https://dialogs.yandex.ru/store/api/dialogs2', params={'page': i, 'limit': 100})
                break
            except ConnectionError as e:
                if attempt >= n - 1:
                    raise e
                time.sleep(2 ** attempt)
        assert r.status_code == 200
        j = r.json()
        all_items.extend(j['result']['items'])
        if not j['result']['hasMore']:
            break
    docs = {item['id']: item for item in all_items if item['channel'] == 'aliceSkill'}
    return docs
