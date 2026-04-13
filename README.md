# Customer-Churn-Prediction

This is a machine learning project that predicts whether a customer will churn or not based on their details. I built this project to understand how different classification models perform on the same dataset and how we can deploy a simple ML model using Streamlit.

What this project does
Takes customer data as input
Cleans and processes the data
Trains different machine learning models
Compares their accuracy
Uses the best model to make predictions
Shows results using a Streamlit web app
Models I used
Logistic Regression
KNN (K-Nearest Neighbors)
SVM (Support Vector Machine)
Decision Tree
Random Forest
Model Results
Model	Accuracy
Logistic Regression	0.865
SVM	0.86
KNN	0.85
Random Forest	0.85
Decision Tree	0.82

So I selected Logistic Regression as the final model since it gave the best accuracy and is also simple to understand.

Tools & Technologies
Python
Pandas & NumPy
Scikit-learn
Streamlit
How it works
Load dataset
Do basic preprocessing (cleaning, encoding, scaling)
Train multiple models
Compare accuracy
Save the best model
Use Streamlit to take user input and predict churn
Streamlit App

In the app, the user can:

Enter customer details
Click predict
Get output as Churn / Not Churn
