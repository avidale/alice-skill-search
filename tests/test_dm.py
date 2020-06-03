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
    resp = mock_dm.respond(make_context('найди навык про воду'))
    assert 'Время выпить воды' in resp.text
