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
