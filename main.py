import logging
import tgalice
import os
from pymongo import MongoClient
import mongomock
import sentry_sdk

import scraping

from dialog_manager import SearcherDialogManager
from nanosearch.custom_engine import SkillEngine


logging.basicConfig(level=logging.INFO)


BASE_URL = 'https://alice-skill-search.herokuapp.com/'


if os.getenv('SENTRY_DSN', None) is not None:
    sentry_sdk.init(os.environ['SENTRY_DSN'])


if __name__ == '__main__':
    mongo_url = os.environ.get('MONGODB_URI')
    if mongo_url:
        mongo_client = MongoClient(mongo_url)
        mongo_db = mongo_client.get_default_database()
    else:
        mongo_client = mongomock.MongoClient()
        mongo_db = mongo_client.db

    engine = SkillEngine()
    print('Scraping...')
    docs = scraping.collect_docs()
    print('Building search indexes...')
    engine.add_docs(docs)

    dm = SearcherDialogManager(engine=engine)

    connector = tgalice.dialog_connector.DialogConnector(
        dialog_manager=dm,
        storage=tgalice.session_storage.MongoBasedStorage(database=mongo_db, collection_name='sessions'),
        log_storage=tgalice.storage.message_logging.MongoMessageLogger(
            collection=mongo_db.get_collection('message_logs', write_concern=0, read_concern=0),
            not_log_id={'9DFE01079196E4602D3CC3BA2B0E030B39C3802AEDEEC2CE6FF1B40F78C5DA3C'},
            detect_pings=True,
        ),
    )
    server = tgalice.server.flask_server.FlaskServer(
        connector=connector, base_url=BASE_URL
    )
    server.parse_args_and_run()
