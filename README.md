# Credit-card-fraud-detection-model
Credit Card Fraud Detection is a machine learning project that predicts whether a credit card transaction is genuine or fraudulent. It uses data preprocessing, feature scaling, and classification algorithms to improve accuracy. A Streamlit interface provides users with quick and reliable fraud predictions.
# 💳 Credit Card Fraud Detection Using Machine Learning

## 📌 Project Overview

This project is a Machine Learning-based application that detects whether a credit card transaction is **Fraudulent** or **Legitimate**. It analyzes transaction details such as transaction amount, transaction hour, foreign transaction status, location mismatch, device trust score, transaction velocity, and cardholder age to make accurate predictions.

The project compares multiple machine learning algorithms and selects the **Decision Tree Classifier** as the final model. The trained model is deployed using **Streamlit**, allowing users to perform real-time fraud detection through a simple web interface.

---

## 🚀 Features

- Data preprocessing and visualization
- Feature scaling using StandardScaler
- Comparison of multiple ML algorithms
- Decision Tree Classifier as the final model
- Real-time fraud prediction
- User-friendly Streamlit interface
- Model saving using Joblib

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## 🤖 Machine Learning Algorithms

- K-Nearest Neighbors (KNN)
- Gaussian Naive Bayes
- Decision Tree Classifier ✅
- Support Vector Machine (SVM)

---

## 📂 Dataset

Dataset: **credit_card.csv**

### Features

- Amount
- Transaction Hour
- Foreign Transaction
- Location Mismatch
- Device Trust Score
- Velocity Last 24 Hours
- Cardholder Age
- Merchant Category

### Target

- **0** → Legitimate Transaction
- **1** → Fraudulent Transaction

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Credit-Card-Fraud-Detection.git
```

Go to the project folder:

```bash
cd Credit-Card-Fraud-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Credit-Card-Fraud-Detection/
│
├── app.py
├── credit_card_model.py
├── credit_card.csv
├── credit_card.pkl
├── scaler.pkl
├── feature_names.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 📊 Workflow

1. Load Dataset
2. Data Preprocessing
3. Feature Encoding
4. Feature Scaling
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Save Model with Joblib
9. Deploy using Streamlit
10. Predict Fraud

---

## 📈 Evaluation Metrics

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 🎯 Prediction

Users enter transaction details through the Streamlit interface.

The model predicts whether the transaction is:

- ✅ Legitimate
- ❌ Fraudulent

---

## 📸 Screenshots

Add screenshots of:

- Dataset
- Data Visualization
- Streamlit Home Page
- Prediction Result

---

## 🔮 Future Improvements

- Deploy on the cloud
- Add deep learning models
- Real-time banking integration
- Explainable AI (XAI)
- Improve accuracy with ensemble methods

---

## 👨‍💻 Author

**Nitika**

Machine Learning Project

---

## 📄 License

This project is created for educational and learning purposes.
