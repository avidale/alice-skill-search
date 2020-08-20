import pytest
from tests.test_data import mock_docs  # noqa

from tgalice.testing.testing_utils import make_context

from skill.dialog_manager import SearcherDialogManager
from nanosearch.custom_engine import SkillEngine


@pytest.fixture()
def mock_engine(mock_docs):
    engine = SkillEngine()
    engine.add_docs(mock_docs)
    return engine


@pytest.fixture()
def mock_dm(mock_engine):
    dm = SearcherDialogManager(engine=mock_engine)
    return dm


def test_greetings(mock_dm: SearcherDialogManager):
    resp = mock_dm.respond(make_context('', new_session=True))
    assert resp.text.startswith('Привет! Это навык "Искатель навыков" для поиска других навыков.')


def test_search(mock_dm: SearcherDialogManager):
    # expect serp
    resp = mock_dm.respond(make_context('найди навык про воду'))
    assert 'Время выпить воды' in resp.text
    assert '1' in resp.suggests

    # expect skill card
    ctx1 = make_context('расскажи подробнее про первый навык', prev_response=resp)
    resp1 = mock_dm.respond(ctx1)
    assert 'Время выпить воды' in resp1.text
    assert 'вести учет выпитой воды' in resp1.text
    assert 'к списку' in resp1.suggests
    assert len(resp1.links) == 1


def test_single_pass(mock_dm: SearcherDialogManager):
    # expect serp
    resp = mock_dm.respond(make_context('найди навык про воду', new_session=True))
    assert 'Время выпить воды' in resp.text
    assert '1' in resp.suggests
