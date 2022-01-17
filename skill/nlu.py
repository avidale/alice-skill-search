import re
import dialogic


RE_PREFIX = re.compile(
    '(алиса )?'
    '(а )?'
    '(меня интересует )?'
    '(найди |поищи )?'
    '(в )?'
    '(какой |какие |каком )?'
    '((есть|существует) ли (такой )?)?'
    '(навык[ие]? )?'
    '(есть )?'
    '(которы[йе] )?'
    '((может|можно|могут|уме[ею]т|позволя[ею]т) )?'
    '(как )?'
    '(мне )?'
    '(поможет )?'
    '(мне )?'
    '((расскаж[еу]т|рассказать|рассказыва[ею]т(ся)?|говорит) (мне |нам )?)?'
    '(про |о |об |обо )?'
    '(в области )?'
)


def get_search_text(request):
    text = dialogic.basic_nlu.fast_normalize(request)
    match = re.match(RE_PREFIX, text)
    if match:
        text = text[match.span()[1]:]
    return text


RE_PREFIX_DETAULS = re.compile(
    '(алиса )?'
    '(расскажи )?'
    '(про )?'
    '(подробнее )?'
    '(про )?'
    '(навык )?'
)


def get_details_skill(request):
    # todo: use this function for item selector
    text = dialogic.basic_nlu.fast_normalize(request)
    match = re.match(RE_PREFIX_DETAULS, text)
    if match:
        text = text[match.span()[1]:]
    return text


RE_EXACT_DETAILS = re.compile(
    '^'
    '(алиса )?'
    '(расскажи )?'
    '(подробнее )?'
    '(про )?'
    '(навык )?'
    '(номер )?'
    '(?P<item>(\\d+|первый|второй|третий|четвертый|пятый|шестой|седьмой|восьмой|девятый|десятый))'
    '( номер)?'
    '( навык)?'
    '$'
)


def get_exact_details_skill(request):
    text = dialogic.basic_nlu.fast_normalize(request)
    match = re.match(RE_EXACT_DETAILS, text)
    if not match:
        return None
    gd = match.groupdict()
    if 'item' not in gd:
        return None
    item = gd['item']
    norms = {
        'первый': 1,
        'второй': 2,
        'третий': 3,
        'четвертый': 4,
        'пятый': 5,
        'шестой': 6,
        'седьмой': 7,
        'восьмой': 8,
        'девятый': 9,
        'десятый': 10,
    }
    return int(norms.get(item, item))
