import re
import spacy

nlp_en = spacy.load("en_core_web_sm")
nlp_ru = spacy.load("ru_core_news_sm")

stopwords_en = nlp_en.Defaults.stop_words
stopwords_ru = nlp_ru.Defaults.stop_words

def preprocess(text):

    text = text.lower()
    text = re.sub(r"[^a-zа-яё\s]", "", text)
    tokens = text.split()
    tokens = [
        t for t in tokens 
        if t not in stopwords_en and t not in stopwords_ru
    ]
    return tokens