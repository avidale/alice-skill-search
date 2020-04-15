from collections import Counter
from nanosearch.simple_searcher import Searcher


class SkillEngine:
    def __init__(self):
        self.docs = {}
        self.par2doc = {}
        self.paragraphs = {}
        self.searcher: Searcher = Searcher()

    def add_docs(self, docs):
        self.docs = docs
        self.par2doc = {}
        self.paragraphs = {}

        for doc_id, doc in docs.items():
            pars = list()
            pars.append(doc['name'])
            pars.append(doc['description'])
            for eg in doc['examples2']:
                pars.append(eg['activationPhrase'])
                pars.append(eg['request'])
            pars = [p for p in pars if p]
            for p in pars:
                p_id = len(self.paragraphs)
                self.par2doc[p_id] = doc_id
                self.paragraphs[p_id] = p
        self.searcher.fit(paragraphs=self.paragraphs)

    def find(self, text, add_scores=False):
        top = self.searcher.get_okapis(text)
        cntr = Counter()
        for par_id, par_score in top.most_common():
            doc_id = self.par2doc[par_id]
            if add_scores or doc_id not in cntr:
                cntr[doc_id] += par_score
        docs = [self.docs[doc_id] for doc_id, score in cntr.most_common()]
        return docs
