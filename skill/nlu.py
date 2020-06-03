import re
import tgalice


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
    text = tgalice.basic_nlu.fast_normalize(request)
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
    text = tgalice.basic_nlu.fast_normalize(request)
    match = re.match(RE_PREFIX_DETAULS, text)
    if match:
        text = text[match.span()[1]:]
    return text
