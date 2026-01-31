import streamlit as st
from transformers import pipeline
import PyPDF2

st.title("⚖️ AI Advocate: Legal Document Summarizer")

# Upload PDF
uploaded_file = st.file_uploader("Upload a legal document (PDF)", type="pdf")

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    st.subheader("Extracted Text")
    st.write(text[:1000] + "..." if len(text) > 1000 else text)

    # Summarization
    st.subheader("AI Summary")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    st.success(summary[0]['summary_text'])
