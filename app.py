import streamlit as st
from preprocess import preprocess
from title_generator import generate_title
from tfidf import compute_tf, compute_df, compute_idf, compute_tfidf

st.title("Keyword Extractor (TF-IDF)")

text = st.text_area("Paste your text here:")

if st.button("Extract keywords"):
    tokens = preprocess(text)

    docs = [tokens]  # for now, single document
    df = compute_df(docs)
    idf = compute_idf(df, len(docs))

    tf = compute_tf(tokens)
    tfidf = compute_tfidf(tf, idf)

    keywords = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)

    for word, score in keywords[:10]:
        st.write(f"**{word}** → {score:.4f}")

    keyword_scores = dict(keywords[:10])
    title = generate_title(text, keyword_scores)

    st.subheader("Suggested Title")
    st.write(title)

    top_keywords = [w for w, _ in keywords[:10]]
