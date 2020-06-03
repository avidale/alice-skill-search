from skill import nlg, nlu
import random
import tgalice
import yaml

from tgalice.dialog_manager import BaseDialogManager
from nanosearch.custom_engine import SkillEngine


class SearcherDialogManager(BaseDialogManager):
    def __init__(
            self,
            engine: SkillEngine,
            faq_file='config/faq.yaml',
            intents_file='config/intents.yaml'
    ):
        super(SearcherDialogManager, self).__init__()
        self.engine = engine

        with open(intents_file, 'r', encoding='utf-8') as f:
            intents = yaml.safe_load(f)
        self.intent_matcher = make_joint_matcher(
            base_matcher=tgalice.nlu.matchers.TFIDFMatcher(),
            intents=intents,
        )
        self.faq_dm = tgalice.dialog_manager.faq.FAQDialogManager(
            faq_file, matcher='cosine',
        )

    def respond(self, ctx: tgalice.dialog.Context):
        uo = ctx.user_object or {}

        text = tgalice.nlu.basic_nlu.fast_normalize(ctx.message_text)
        intents = self.intent_matcher.aggregate_scores(text)
        faq_response = self.faq_dm.try_to_respond(ctx)

        if ctx.session_is_new() or not ctx.message_text or ctx.message_text == '/start':
            resp_text = 'Привет! Это навык "Искатель навыков" для поиска других навыков. ' \
                        'Можете спросить меня, например, "Какой навык рассказывает про костный мозг?" ' \
                        'Чтобы выйти, скажите "Алиса, хватит"'
            return tgalice.dialog.Response(resp_text)
        elif tgalice.basic_nlu.like_help(ctx.message_text):
            resp_text = 'Вы в навыке "Искатель навыков" для поиска других навыков. ' \
                        'Можете спросить меня, например, "Какой навык рассказывает про костный мозг?" ' \
                        'Чтобы выйти, скажите "Алиса, хватит"'
            return tgalice.dialog.Response(resp_text, suggests=['Хватит'])
        elif tgalice.basic_nlu.like_exit(ctx.message_text) or 'exit_skill' in intents:
            resp_text = 'Всего доброго! Чтобы вернуться в навык, ' \
                        'скажите "Алиса, включи навык "Искатель навыков".'
            return tgalice.dialog.Response(resp_text, commands=[tgalice.COMMANDS.EXIT])
        elif 'run_skill' in intents:
            resp_text = random.choice([
                'Чтобы запускать другие навыки, вам нужно сначала выйти из этого.',
                'Чтобы запустить другой навык, сначала покиньте этот.',
                'Для запуска других навыков вам нужно вернуться к Алисе. Скажите "хватит", чтобы выйти.',
            ])
            return tgalice.dialog.Response(resp_text, suggests=['Хватит'])
        elif faq_response:
            faq_response.updated_user_object = uo
            return faq_response

        search_text = nlu.get_search_text(ctx.message_text)
        results = self.engine.find(search_text)
        if not results:
            resp_text = 'Простите, ничего не нашла по запросу "{}".'.format(search_text)
            return tgalice.dialog.Response(resp_text)
        uo['found_skills'] = [doc['id'] for doc in results]
        resp_text = 'Нашла {} навыков:'.format(len(results))
        links = []
        for i, doc in enumerate(results[:3]):
            resp_text = resp_text + '\n {}: {};'.format(
                i+1,
                nlg.skill_title(doc),
            )
            links.append({
                'title': doc['name'],
                'hide': False,
                'url': 'https://alice.ya.ru/s/{}'.format(doc['id']),
            })
        response = tgalice.dialog.Response(resp_text, links=links, user_object=uo)
        return response


def make_joint_matcher(base_matcher: tgalice.nlu.matchers.BaseMatcher, intents):
    # todo: integrate it to TgAlice
    labels = []
    texts = []
    re_labels = []
    re_texts = []
    for intent_name, intent in intents.items():
        if 'regexp' in intent:
            exps = intent['regexp']
            if not isinstance(exps, list):
                exps = [exps]
            for exp in exps:
                re_labels.append(intent_name)
                re_texts.append(exp)
        if 'examples' in intent:
            for ex in intent['examples']:
                labels.append(intent_name)
                texts.append(ex)
    base_matcher.fit(texts, labels)
    re_matcher = tgalice.nlu.matchers.RegexMatcher()
    re_matcher.fit(re_texts, re_labels)
    return tgalice.nlu.matchers.MaxMatcher([base_matcher, re_matcher])
