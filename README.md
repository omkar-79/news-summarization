![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
# 📰 News Summarization using T5 Model

This project implements a **news summarization system** using the **T5-base** model, fine-tuned on the **CNN/DailyMail** dataset from Hugging Face. The project covers data pre-processing, exploratory data analysis (EDA), model fine-tuning, and evaluation using ROUGE scores.

---

## 📚 Dataset Information

Dataset used: [CNN/DailyMail](https://huggingface.co/datasets/abisee/cnn_dailymail)

- **Train Size:** 287,113 samples  
- **Validation Size:** 13,368 samples  
- **Test Size:** 11,490 samples  

---

## 🖥️ Web Dashboard

![WebApp Screenshot](https://i.imgur.com/t3QIc1Y.jpeg)

---

## 📊 Evaluation Results

| Metric      | Score  |
|-------------|--------|
| ROUGE-1     | 0.2969 |
| ROUGE-2     | 0.1204 |
| ROUGE-L     | 0.2483 |
| ROUGE-Lsum  | 0.2483 |


## 🛠️ Project Setup

### 1. **Clone the repository:**
```bash
git clone https://github.com/omkar-79/news-summarization.git
cd news-summarization
```

### 2. **Create a virtual environment (Optional):**
```
# For Python 3.x
python3 -m venv venv
source venv/bin/activate    # On Linux/Mac
# OR
venv\Scripts\activate       # On Windows
```

### 3. **Install required packages:**
```
pip install -r requirements.txt
```

### 4. **Run the Jupyter Notebook:**
- Open the .ipynb file using Jupyter Notebook or Jupyter Lab.
- Run all the cells to fine-tune the model.
- The fine-tuned model will be saved to:
```
./t5_finetuned
```

### 5. **Run the Flask Application:**
```
python app.py
```

### 6. **Open the Interface:**
After running app.py, open index.html in your browser to access the application.
