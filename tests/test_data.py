import copy
import pytest


null = None
true = True
false = False

docs = [
    {
        "name": "Да, милорд",
        "description": "Милорд! Король поручает Вам управление нашими землями! "
                       "Удерживайте баланс между своим влиянием и богатством, "
                       "иначе король непременно казнит Вас.\n\n"
                       "Выбирайте лучшую стратегию и принимайте неожиданные решения "
                       "в самых запутанных ситуациях, чтобы удержаться у власти как можно дольше!\n\n"
                       "Игра создана на платформе aimylogic.com",
        "developerName": "Dima Che",
        "examples2": [
            {
                "marker": "запусти навык",
                "activationPhrase": "Да милорд",
                "request": ""
            },
            {
                "marker": "давай поиграем в",
                "activationPhrase": "Да милорд",
                "request": ""
            },
            {
                "marker": "поиграем в",
                "activationPhrase": "Да милорд",
                "request": ""
            }
        ],
        "id": "cd48fd87-0181-4fb1-bbc8-f95c819846bd",
        "category": "games_trivia_accessories",
        "categoryLabel": "Игры и развлечения",
        "channel": "aliceSkill",
        "color": "#B00000",
        "examples": [
            "запусти навык Да милорд",
            "давай поиграем в Да милорд",
            "поиграем в Да милорд"
        ],
        "isRecommended": true,
        "logo": "https://avatars.mds.yandex.net/get-dialogs/758954/1a309e8e7d6781214dc5/orig",
        "surfaces": [
            "desktop",
            "mobile",
            "auto",
            "navigator",
            "station"
        ],
        "slug": "c358af99-da-milord",
        "rating": [
            445,
            131,
            244,
            637,
            3122
        ],
        "botGuid": null,
        "openInNewTab": true,
        "explicitContent": false,
        "responseTime": null,
        "trusted": false,
        "donationSettings": null,
        "alicePrizeNomination": null,
        "alicePrizeRecievedAt": "2018-11-24T21:00:00.000Z"
    },
    {
        "name": "Музыкальные стулья",
        "description": "🏆 Это веселая игра из детства. "
                       "Вокруг стульев по кругу бегут участники, "
                       "и когда заканчивается музыка — надо успеть сесть на стул. "
                       "И одному игроку всегда не хватает места. "
                       "Алиса возьмет на себя роль озорного ведущего.\n"
                       "Отлично подойдет для игры с детьми или для веселой компании взрослых. "
                       "Развлекайтесь! :))\n"
                       "Лауреат премии Алисы. Сделано на Aimylogic.",
        "developerName": "Сергей Кул (GarEngin)",
        "examples2": [
            {
                "marker": "запусти навык",
                "activationPhrase": "Музыкальные стулья",
                "request": ""
            },
            {
                "marker": "давай сыграем в",
                "activationPhrase": "Музыкальные стулья",
                "request": ""
            },
            {
                "marker": "давай поиграем в",
                "activationPhrase": "Музыкальные стулья",
                "request": ""
            }
        ],
        "id": "5043c1f0-affb-4c7f-87fa-67f1fa52e461",
        "category": "games_trivia_accessories",
        "categoryLabel": "Игры и развлечения",
        "channel": "aliceSkill",
        "color": "#902048",
        "examples": [
            "запусти навык Музыкальные стулья",
            "давай сыграем в Музыкальные стулья",
            "давай поиграем в Музыкальные стулья"
        ],
        "isRecommended": true,
        "logo": "https://avatars.mds.yandex.net/get-dialogs/758954/122ba67c3e32727c2603/orig",
        "surfaces": [
            "desktop",
            "mobile",
            "auto",
            "navigator",
            "station"
        ],
        "slug": "e64a2748-muzykal-nye-stul-ya",
        "rating": [
            47,
            16,
            17,
            27,
            483
        ],
        "botGuid": null,
        "openInNewTab": true,
        "explicitContent": false,
        "website": "http://garengin.ru",
        "responseTime": null,
        "trusted": false,
        "donationSettings": {
            "defaultSum": "50",
            "walletNumber": "410019952549892"
        },
        "alicePrizeNomination": "kids",
        "alicePrizeRecievedAt": "2019-08-24T21:00:00.000Z"
    },
    {
        "name": "Одно из двух",
        "description": "Одна из самых популярных игр на западе! "
                       "Подойдет как для веселой компании, так и для одного. "
                       "Я задаю неожиданные вопросы и предлагаю выбрать одно из двух. "
                       "Посмотрим, насколько часто твои ответы будут соответствовать "
                       "ответам большинства других игроков!",
        "developerName": "Dima Che & Discodasha",
        "examples2": [
            {
                "marker": "запусти навык",
                "activationPhrase": "Одно из двух",
                "request": ""
            },
            {
                "marker": "давай поиграем в",
                "activationPhrase": "Одно из двух",
                "request": ""
            },
            {
                "marker": "давай поиграем в",
                "activationPhrase": "1 из 2",
                "request": ""
            }
        ],
        "id": "99d0d893-046d-4bfb-b273-d9cf8d026e18",
        "category": "games_trivia_accessories",
        "categoryLabel": "Игры и развлечения",
        "channel": "aliceSkill",
        "color": "#000000",
        "examples": [
            "запусти навык Одно из двух",
            "давай поиграем в Одно из двух",
            "давай поиграем в 1 из 2"
        ],
        "isRecommended": true,
        "logo": "https://avatars.mds.yandex.net/get-dialogs/1027858/27e0f9c650f4fb5271d6/orig",
        "surfaces": [
            "desktop",
            "mobile",
            "auto",
            "navigator",
            "station"
        ],
        "slug": "69a22df1-odno-iz-dvuh",
        "rating": [
            118,
            48,
            116,
            355,
            1874
        ],
        "botGuid": null,
        "openInNewTab": true,
        "explicitContent": false,
        "responseTime": null,
        "trusted": false,
        "donationSettings": null,
        "alicePrizeNomination": null,
        "alicePrizeRecievedAt": "2018-12-24T21:00:00.000Z"
    },
    {
        "name": "Время выпить воды!",
        "description": "Почему нужно пить воду?\n\n"
                       "Вода является наиболее важным источником энергии в нашем организме. "
                       "Она даёт жизнь и невероятным образом спасает от многих недугов.\n\n"
                       "Но очень часто мы забываем пить воду или пьем ее недостаточно.\n\n"
                       "Навык \"Время выпить воды!\" поможет вам правильно определить цель "
                       "по количеству необходимой жидкости и вести учет выпитой воды.",
        "developerName": "Adel",
        "examples2": [
            {
                "marker": "запусти навык",
                "activationPhrase": "Время выпить воды",
                "request": ""
            }
        ],
        "id": "a0c952e9-8082-4924-ba8e-f2438bc5cb28",
        "category": "health_fitness",
        "categoryLabel": "Спорт и здоровье",
        "channel": "aliceSkill",
        "color": "#F8F8F8",
        "examples": [
            "запусти навык Время выпить воды"
        ],
        "isRecommended": true,
        "logo": "https://avatars.mds.yandex.net/get-dialogs/1525540/d524197d6dc2dce7c16a/orig",
        "surfaces": [
            "desktop",
            "mobile",
            "auto",
            "navigator",
            "station"
        ],
        "slug": "593df984-vremya-vypit-vody",
        "rating": [
            36,
            13,
            13,
            29,
            293
        ],
        "botGuid": null,
        "openInNewTab": true,
        "explicitContent": false,
        "responseTime": null,
        "trusted": false,
        "donationSettings": null,
        "alicePrizeNomination": "special",
        "alicePrizeRecievedAt": "2019-10-24T21:00:00.000Z"
    }
]


@pytest.fixture()
def mock_docs():
    return {doc['id']: doc for doc in copy.deepcopy(docs)}
