import nlg
import nlu
import tgalice

from tgalice.dialog_manager import BaseDialogManager
from nanosearch.custom_engine import SkillEngine


class SearcherDialogManager(BaseDialogManager):
    def __init__(self, engine: SkillEngine):
        super(SearcherDialogManager, self).__init__()
        self.engine = engine

    def respond(self, ctx: tgalice.dialog.Context):
        uo = ctx.user_object or {}
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
        elif tgalice.basic_nlu.like_exit(ctx.message_text):
            resp_text = 'Всего доброго! Чтобы вернуться в навык, ' \
                        'скажите "Алиса, включи навык "Искатель навыков".'
            return tgalice.dialog.Response(resp_text, commands=[tgalice.COMMANDS.EXIT])
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
