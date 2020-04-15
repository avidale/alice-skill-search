import razdel


def jaccard(s1, s2):
    s1 = set(s1.lower().split())
    s2 = set(s2.lower().split())
    num = len(s1.intersection(s2))
    if not num:
        return 0.0
    return num / len(s1.union(s2))


def skill_title(doc):
    title = doc['name']
    description_long = doc['description']
    sents = list(razdel.sentenize(description_long))
    description_short = sents[0].text
    if jaccard(title, description_short) < 0.5:
        return '{} ({})'.format(title, description_short)
    return title
