import streamlit as st
from preprocess import preprocess
from tfidf import compute_tf, compute_df, compute_idf, compute_tfidf
from title_generator import generate_title

st.title("Извлечение ключевых слов (TF-IDF)")
st.caption("TF-IDF на корпусе документов")

num_docs = st.number_input(
    "Количество документов",
    min_value=2,
    max_value=10,
    value=3,
    step=1
)

docs_text = []
for i in range(num_docs):
    text = st.text_area(
        f"Документ {i + 1}",
        height=150,
        key=f"doc_{i}"
    )
    docs_text.append(text)

doc_index = st.selectbox(
    "Выберите документ для анализа",
    options=list(range(1, num_docs + 1))
) - 1

if st.button("Извлечь ключевые слова"):
    if any(not d.strip() for d in docs_text):
        st.warning("Все документы должны быть заполнены")
        st.stop()

    docs_tokens = [preprocess(doc) for doc in docs_text]

    df = compute_df(docs_tokens)
    idf = compute_idf(df, len(docs_tokens))

    tf = compute_tf(docs_tokens[doc_index])
    tfidf = compute_tfidf(tf, idf)

    keywords = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)

    st.subheader(f"Ключевые слова — Документ {doc_index + 1}")
    for word, score in keywords[:10]:
        st.write(f"**{word}** → {score:.4f}")
