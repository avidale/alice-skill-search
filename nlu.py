import re
import tgalice


RE_PREFIX = re.compile(
    '(алиса )?'
    '(какой )?'
    '(навык )?'
    '(который )?'
    '((может|умеет) )?'
    '(как )?'
    '(мне )?'
)


def get_search_text(request):
    text = tgalice.basic_nlu.fast_normalize(request)
    match = re.match(RE_PREFIX, text)
    if match:
        text = text[match.span()[1]:]
    return text
