from collections import Counter
from typing import Dict

class BaseSearcher:
    def fit(self, paragraphs: Dict):
        """ Add paragraphs to the search index.
        :param paragraphs: Dict[paragraph_id, paragraph_text]
        """
        raise NotImplementedError()

    def get_candidates(self, query: str, n: int = None) -> Counter:
        """ Retrieve top n candidates along with their scores """
        raise NotImplementedError()
