import pytest

from skill.nlu import get_search_text, get_details_skill, get_exact_details_skill


@pytest.mark.parametrize('text_in,text_out', [
    ('алиса какой навык записывать в тебя заметки', 'записывать в тебя заметки'),
    ('алиса какие навыки включают тебя заметки', 'включают тебя заметки'),
    ('Какой навык расскажет про погоду', 'погоду'),
    ('а какие навыки есть в области математики', 'математики'),
    ('какой навык рассказывает о кошках', 'кошках'),
    ('навык который рассказывает о кошках', 'кошках'),
    ('навык про голосовые помощники', 'голосовые помощники'),
    ('какой навык позволяет делать покупки на беру', 'делать покупки на беру'),
    ('найди навык про космос', 'космос'),
    ('в каком навыке есть пошлые фотки', 'пошлые фотки'),
])
def test_get_search_text(text_in, text_out):
    assert get_search_text(text_in) == text_out


@pytest.mark.parametrize('text_in,text_out', [
    ('расскажи про подробнее про страна', 'страна'),
    ('расскажи про навык записывать у тебя заметки', 'записывать у тебя заметки'),
])
def test_get_details_skill(text_in, text_out):
    assert get_details_skill(text_in) == text_out


@pytest.mark.parametrize('text_in,text_out', [
    ('расскажи про подробнее про страна', None),
    ('алиса расскажи про второй навык', 2),
    ('23', 23),
    ('подробнее про 23 номер', 23),
])
def test_get_exact_details_skill(text_in, text_out):
    assert get_exact_details_skill(text_in) == text_out
