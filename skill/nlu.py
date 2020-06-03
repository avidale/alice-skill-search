import re
import tgalice


RE_PREFIX = re.compile(
    '(алиса )?'
    '(а )?'
    '(какой |какие )?'
    '(навык |навыки )?'
    '(есть )?'
    '(которы[йе] )?'
    '((может|могут|уме[ею]т|позволя[ею]т) )?'
    '(как )?'
    '(мне )?'
    '((расскаж[еу]т|рассказать|рассказыва[ею]т(ся)?) (мне |нам )?)?'
    '(про |о |об |обо )?'
    '(в области )?'
)


def get_search_text(request):
    text = tgalice.basic_nlu.fast_normalize(request)
    match = re.match(RE_PREFIX, text)
    if match:
        text = text[match.span()[1]:]
    return text
