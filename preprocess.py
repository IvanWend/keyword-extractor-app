import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

stopwords_en = set(stopwords.words("english"))
stopwords_ru = set(stopwords.words("russian"))
STOPWORDS = stopwords_en | stopwords_ru

def preprocess(text):

    text = text.lower()
    text = re.sub(r"[^a-zа-яё\s]", "", text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS]
    return tokens