# Candidate Recommender System

Welcome!  
This project is a smart, user-friendly candidate recommender system that helps recruiters and hiring managers efficiently match job descriptions with the most relevant resumes. It leverages modern NLP and machine learning tools to streamline the hiring process.

---

## 🚀 Features

- **Resume & Job Description Parsing:** Upload resumes (PDF/DOCX) and paste job descriptions.
- **Semantic Matching:** Uses state-of-the-art NLP (spaCy, Sentence Transformers) for accurate candidate-job fit.
- **Easy-to-Use Interface:** Simple web app powered by Streamlit.
- **Customizable:** Easily extendable for new features or different matching logic.

---

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit
- spaCy
- scikit-learn
- sentence-transformers
- nltk
- python-docx
- pdfminer.six

---

## 📦 Installation

### 1. **Clone the repository**
```git clone https://github.com/rohans9/candidate-recommender-system.git```
```cd candidate-recommender-system```

### 2. **Create and activate a virtual environment**  
This keeps our dependencies isolated and our system clean.

- **Windows:**
```python -m venv venv```
venv\Scripts\activate

### 3. **Install dependencies**
```pip install -r requirements.txt```

### 4. **Download the spaCy English model**
```python -m spacy download en_core_web_lg```


---

## 🏃‍♂️ Usage

1. **Start the app:**
```streamlit run main.py```


2. **How it works:**
- Paste your job description in the provided field.
- Upload one or more candidate resumes (PDF or DOCX).
- Click "Recommend" to see the best-matching candidates, ranked by fit score.

---

## 📁 Project Structure

candidate-recommender-system/
│
├── main.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── README.md
└── ... 


---

## 🧹 Best Practices

- **Use a virtual environment for every project** to avoid dependency conflicts and keep your system Python clean.
- **Track dependencies** with `requirements.txt` for easy setup and reproducibility.
- **Add `venv/` to your `.gitignore`** file so you don’t commit your virtual environment to version control.

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome!  
Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open-source  and available under the [MIT License](LICENSE).

---

## 🙋 FAQ

**Q: Do I need a virtual environment?**  
A: Yes, it’s highly recommended for dependency isolation and reproducibility.

**Q: Can I use other file formats for resumes?**  
A: Currently, PDF and DOCX are supported. You can extend the code for more formats!

**Q: How does the matching work?**  
A: The system uses semantic text embeddings and similarity scoring to match resumes to job descriptions.

---

*Made with ❤️ by Rohan Sahu*

