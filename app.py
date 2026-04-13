#Gender 1->Male and 0->Female
#Churn 1->Yes and 0->No
#scaler is exported as scaler.pkl

import streamlit as st
import joblib
import numpy as np

st.title("Churn Prediction App")
st.divider()

st.write("Please Enter The Values And Hit The Predict Button For Getting Prediction")
st.divider()

age=st.number_input("Enter Age:",min_value=10,max_value=100,value=30)
tenure=st.number_input("Enter Tenure:",min_value=0,max_value=130,value=10)
monthlycharge=st.number_input("Enter Monthly Charge:",min_value=0,max_value=150)
gender=st.selectbox("Enter the Gender:",["Male","Female"])
st.divider()

scaler=joblib.load("scaler.pkl")
model=joblib.load("churn_model.pkl")

predictbutton=st.button("Predict")

if predictbutton:
    gender_selected=1 if "Female" else 0
    X=[age,gender_selected,tenure,monthlycharge]
    X1=np.array(X)
    X_array=scaler.transform([X1])
    prediction=model.predict(X_array)[0]

    st.balloons()

    predicted="Churn" if prediction==1 else "Not Churn"
    st.write(predicted)

else:
    st.write("Please Enter All The Values And Then Click Predict.")

