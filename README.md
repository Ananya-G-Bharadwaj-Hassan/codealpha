# 🚗 Car Price Prediction using Machine Learning

## 📌 Project Overview

The Car Price Prediction project is a machine learning application that predicts the selling price of a used car based on its specifications such as manufacturing year, present price, kilometers driven, fuel type, seller type, transmission type, and number of previous owners.

The model is trained using historical car sales data and deployed using **Streamlit**, allowing users to interact with the model through a simple web interface. The Streamlit app loads a trained Random Forest model and predicts the estimated selling price based on user input. :contentReference[oaicite:0]{index=0}

---

## 🎯 Objectives

- Predict the selling price of a used car.
- Perform data preprocessing and feature engineering.
- Train and evaluate multiple regression models.
- Deploy the model using Streamlit.

---

## 📂 Dataset

The dataset contains information about used cars with features such as:

- Year
- Present Price
- Driven Kilometers
- Fuel Type
- Seller Type
- Transmission
- Owner
- Selling Price (Target Variable)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Pickle

---

## 📊 Machine Learning Workflow

### 1. Data Collection

- Load the dataset.
- Explore the features and target variable.

### 2. Data Preprocessing

- Handle categorical variables.
- Encode categorical features.
- Remove unnecessary columns.
- Split data into training and testing datasets.

### 3. Model Training

Random Forest Regressor

### 4. Model Evaluation

Evaluation Metrics:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The Random Forest Regressor was selected because it provided the best prediction performance.

---

## 🚀 Streamlit Application

The application allows users to enter:

- Manufacturing Year
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Number of Previous Owners

The trained Random Forest model predicts the estimated selling price instantly. :contentReference[oaicite:1]{index=1}

---

## 📁 Project Structure

```
Car-Price-Prediction/
│
├── CarPricePrediction.ipynb
├── app.py
├── model.pkl
├── car data.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/Car-Price-Prediction.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit app

```bash
cd CarPricePrediction
streamlit run app.py
```

---

## 📈 Features

- Predicts used car selling prices.
- Interactive Streamlit interface.
- Fast and accurate predictions.
- User-friendly input form.
- Real-time price estimation.

---

## Future Improvements

- Deploy on Streamlit Cloud or Render.
- Add more vehicle features.
- Improve prediction accuracy using advanced ensemble models.
- Integrate external APIs for live market prices.

---

## Skills Demonstrated

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Regression Models
- Random Forest
- Model Evaluation
- Streamlit Deployment
- Machine Learning Pipeline

---
