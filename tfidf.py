import math
from preprocess import preprocess
from collections import Counter, defaultdict

def compute_tf(tokens):
    counts = Counter(tokens)
    total = sum(counts.values())
    return {w: c / total for w, c in counts.items()}

def compute_df(docs):
    df = defaultdict(int)
    for doc in docs:
        for word in set(doc):
            df[word] += 1
    return df

def compute_idf(df, n_docs):
    return {
        w: math.log((n_docs + 1) / (df[w] + 1)) + 1
        for w in df
    }

def compute_tfidf(tf, idf):
    return {w: tf[w] * idf.get(w, 0.0) for w in tf}
