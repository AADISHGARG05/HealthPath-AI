# 🧠 HealthPath AI – Intelligent Disease Prediction from Symptoms

![HealthPath AI](https://img.shields.io/badge/HealthPath-AI-green?style=for-the-badge&logo=medical-services)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-yellow?style=for-the-badge&logo=javascript)
![ML Model](https://img.shields.io/badge/Model-Logistic%20Regression-purple?style=for-the-badge&logo=scikit-learn)

## 🌐 Live Demo
> Coming Soon...

---

## 📌 Description

**HealthPath AI** is an AI-driven web application that empowers users to predict possible diseases based on the symptoms they are experiencing. Users select 3 to 15 symptoms, and the ML model returns the most probable diseases, confidence percentages, and insights.

> **Disclaimer:** This tool is intended for educational and informational purposes only. It is not a substitute for professional medical advice.

---

## 🩺 Features

✅ Easy-to-use and intuitive symptom selection  
✅ Categorized symptoms (Respiratory, Neurological, Skin, etc.)  
✅ Real-time disease prediction using trained ML model  
✅ Displays top 3 disease predictions with confidence scores  
✅ Responsive, modern UI with animations and smooth transitions  
✅ Backend integration using Flask API  
✅ Completely offline and secure – no data storage  
✅ Extensible for SHAP-based interpretability (future)

---

## 🖥️ Screenshots

<img src="screenshots/homepage.png" width="100%" alt="Home Page"/>
<img src="screenshots/symptoms.png" width="100%" alt="Symptoms Selection"/>
<img src="screenshots/prediction.png" width="100%" alt="Prediction Results"/>

---

## 🚀 Technologies Used

| Frontend         | Backend        | Machine Learning         | Deployment Ready |
|------------------|----------------|---------------------------|------------------|
| HTML, CSS, JS    | Flask (Python) | Logistic Regression       | Localhost / Render / AWS |
| FontAwesome Icons| REST API       | Label Encoding, Scaling   |                  |

---

## 📁 Project Structure

HealthPath-AI/
│
├── static/ # Static files (CSS, JS)
│ └── style.css
│
├── templates/ # HTML Templates
│ └── index.html
│
├── model/ # ML model and encoder
│ ├── logistic_model.pkl
│ └── label_encoder.pkl
│
├── symptom_list.txt # List of all training symptoms
├── app.py # Flask backend
├── README.md # This file

## 📈 ML Model Details

- **Model Used**: Logistic Regression  
- **Dataset**: Custom dataset with 370+ symptoms across 500+ disease labels  
- **Preprocessing**: One-hot encoding of symptoms  
- **Performance**: 80–85% top-3 accuracy on validation set  

---

## 🛠️ Future Improvements

- ✅ SHAP-based model explanation  
- ✅ Add historical user dashboard  
- ✅ Add medical API integration  
- ✅ Disease severity levels  
- ✅ Mobile app version  
