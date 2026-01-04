import re

def split_sentences(text):
    sentences = re.split(r"[.!?]\s+", text)
    return [s.strip() for s in sentences if len(s.strip()) > 0]

def score_sentences(sentences, keyword_scores):
    scores = []

    for sent in sentences:
        words = sent.lower().split()
        score = sum(keyword_scores.get(w, 0.0) for w in words)
        scores.append((sent, score))

    return scores

def clean_title(title):
    title = title.replace(" are ", " ")
    title = title.replace(" is ", " ")
    title = title.replace(" widely ", " ")
    title = title.replace(",", "")
    return title

def shorten_title(title, max_words=8):
    words = title.split()
    return " ".join(words[:max_words])

def generate_title(text, keyword_scores):
    sentences = split_sentences(text)
    scored = score_sentences(sentences, keyword_scores)

    best_sentence, _ = max(scored, key=lambda x: x[1])

    title = clean_title(best_sentence)
    title = shorten_title(title)

    return title


