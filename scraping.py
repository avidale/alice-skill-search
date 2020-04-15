import requests


def collect_docs():
    all_items = []
    for i in range(1, 100):
        r = requests.get('https://dialogs.yandex.ru/store/api/dialogs2', params={'page': i, 'limit': 100})
        assert r.status_code == 200
        j = r.json()
        all_items.extend(j['result']['items'])
        if not j['result']['hasMore']:
            break
    docs = {item['id']: item for item in all_items if item['channel'] == 'aliceSkill'}
    return docs
