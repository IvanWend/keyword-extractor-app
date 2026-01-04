import re

STOPWORDS = {
    "the", "is", "and", "to", "of", "in", "a", "that", "it", "for", "on", "how"
}

def preprocess(text):

    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS]
    return tokens