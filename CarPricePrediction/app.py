import pickle
import streamlit as st
import pandas as pd
from datetime import datetime

# Load model
rf=pickle.load(open("model.pkl", "rb"))

#streamlit web interface
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

st.title("🚗 Car Price Prediction")
st.write("Enter the car details below to predict its selling price.")

# Inputs
year=st.number_input("Manufacturing Year", 2000, 2025, 2018)

present_price=st.number_input("Present Price (Lakhs)", 0.0, 100.0, 5.0)

kms=st.number_input("Kilometers Driven", 0, 500000, 25000)

fuel=st.selectbox("Fuel Type", ["Petrol","Diesel","CNG"])

seller=st.selectbox("Seller Type", ["Dealer","Individual"])

transmission=st.selectbox("Transmission", ["Manual","Automatic"])

owner=st.selectbox("Number of Previous Owners", [0, 1])

fuel_map={
    "CNG":0,
    "Diesel":1,
    "Petrol":2
}

seller_map={
    "Dealer":0,
    "Individual":1
}

transmission_map={
    "Automatic":0,
    "Manual":1
}

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "Year": [year],
        "Present_Price": [present_price],
        "Driven_kms": [kms],
        "Fuel_Type": [fuel_map[fuel]],
        "Selling_type": [seller_map[seller]],
        "Transmission": [transmission_map[transmission]],
        "Owner": [owner]
    })

#prediction by model
    prediction=rf.predict(input_data)

    predicted_price=max(0, prediction[0])

#printing the prediction
    st.metric(
        label="💰 Estimated Selling Price",
        value=f"₹ {predicted_price:.2f} Lakhs"
    )