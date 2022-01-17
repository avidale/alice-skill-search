import gc
import logging
import random
import threading
import time

import dialogic
import os
from pymongo import MongoClient
import mongomock
import sentry_sdk

from skill import scraping

from skill.dialog_manager import SearcherDialogManager
from nanosearch.custom_engine import SkillEngine


logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)


BASE_URL = 'https://alice-skill-search.herokuapp.com/'


if os.getenv('SENTRY_DSN', None) is not None:
    sentry_sdk.init(os.environ['SENTRY_DSN'])


UPDATE_INTERVAL = 60 * 15  # every 15 minutes


if __name__ == '__main__':
    mongo_url = os.environ.get('MONGODB_URI')
    if mongo_url:
        mongo_client = MongoClient(mongo_url)
        mongo_db = mongo_client.get_default_database()
    else:
        mongo_client = mongomock.MongoClient()
        mongo_db = mongo_client.db

    engine = SkillEngine()

    def update():
        t = time.time()
        print('Scraping...')
        logger.info('Scraping...')
        docs = scraping.collect_docs()
        print('Building search indexes...')
        logger.info('Building search indexes...')
        engine.add_docs(docs)
        print(f'Docs have been updated in {time.time() - t} seconds!')
        logger.info(f'Docs have been updated in {time.time() - t} seconds!')

    print('Running the initial scraping')
    update()

    def update_loop():
        print('START waiting for the update loop')
        logger.info('START waiting for the update loop')
        while True:
            # sleep a random time to unsync workers from each other
            time.sleep(UPDATE_INTERVAL * (0.75 + 0.5 * random.random()))
            print('ENTER the update loop')
            logger.info('ENTER the update loop')
            try:
                update()
            except Exception as e:
                sentry_sdk.capture_exception(e)
            gc.collect()
            print('EXIT the update loop')
            logger.info('EXIT the update loop')

    thread = threading.Thread(target=update_loop, args=())
    thread.daemon = True
    thread.start()

    dm = SearcherDialogManager(engine=engine)

    connector = dialogic.dialog_connector.DialogConnector(
        dialog_manager=dm,
        storage=dialogic.session_storage.MongoBasedStorage(database=mongo_db, collection_name='sessions'),
        log_storage=dialogic.storage.message_logging.MongoMessageLogger(
            collection=mongo_db.get_collection('message_logs', write_concern=0, read_concern=0),
            not_log_id={'9DFE01079196E4602D3CC3BA2B0E030B39C3802AEDEEC2CE6FF1B40F78C5DA3C'},
            detect_pings=True,
        ),
    )
    server = dialogic.server.flask_server.FlaskServer(
        connector=connector, base_url=BASE_URL
    )
    server.parse_args_and_run()
