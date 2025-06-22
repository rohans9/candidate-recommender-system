import streamlit as st
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

nlp = spacy.load("en_core_web_lg")
sbert_model = SentenceTransformer('all-MiniLM-L6-v2')

def parse_resume(file):
    text = ""
    if file.name.endswith('.pdf'):
        from pdfminer.high_level import extract_text
        text = extract_text(file)
    elif file.name.endswith('.docx'):
        from docx import Document
        doc = Document(file)
        text = '\n'.join([para.text for para in doc.paragraphs])
    return text

def process_jd(jd_text):
    doc = nlp(jd_text)
    return ' '.join([token.lemma_ for token in doc if not token.is_stop])

def get_embeddings(texts, model='tfidf'):
    """Generating text embeddings"""
    if model == 'tfidf':
        vectorizer = TfidfVectorizer()
        return vectorizer.fit_transform(texts)
    elif model == 'sbert':
        return sbert_model.encode(texts)
    
def recommend_candidates(jd_text, resumes, top_n=5):
    """Main recommendation function"""

    # Process JD and Resume
    processed_jd = process_jd(jd_text)
    processed_resumes = [process_jd(resume) for resume in resumes]
    
    # Generate embeddings
    jd_embedding = get_embeddings([processed_jd], model='sbert')
    resume_embeddings = get_embeddings(processed_resumes, model='sbert')
    
    # Calculate similarity
    similarities = cosine_similarity(jd_embedding, resume_embeddings)
    
    # Get top candidates
    top_indices = np.argsort(similarities[0])[::-1][:top_n]
    return [(resumes[i], similarities[0][i]) for i in top_indices]

# Streamlit UI
st.title("Candidate Recommender System")
jd = st.text_area("Paste Job Description:")
resumes = st.file_uploader("Upload Resumes (PDF/DOCX):", accept_multiple_files=True)

if st.button("Recommend"):
    if jd and resumes:
        parsed_resumes = [parse_resume(file) for file in resumes]
        recommendations = recommend_candidates(jd, parsed_resumes)
        
        st.subheader("Top Matches:")
        for resume, score in recommendations:
            st.write(f"Match Score: {score:.2f}")
            st.expander("View Resume").write(resume[:1000] + "...")