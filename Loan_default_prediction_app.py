import streamlit as st
import joblib

# Load the model from the pickle file
model = joblib.load(r'C:\\Users\\Padmashree\\Documents\\DADS\\Data science\\Final project\\logreg_model.pkl')

# Streamlit UI
st.title('Loan Defaulters Prediction')

# Define the prediction function
def predict_default(features):
    features_array = [[features[feature] for feature in features]]
    prediction = model.predict(features_array)
    return prediction

# Define input fields for numerical variables
age = st.text_input("Age")
income = st.text_input("Income")
loan_amount = st.text_input("Loan Amount")
credit_score = st.text_input("Credit Score")
months_employed = st.text_input("Months Employed")


# Create a button to trigger the model prediction
if st.button('Predict'):
    
    # Get the values entered by the user
    input_values = {
        'Age': float(age),
        'Income': float(income),
        'LoanAmount': float(loan_amount),
        'CreditScore': float(credit_score),
        'MonthsEmployed': float(months_employed)
    }
    
    # Use the input values for prediction
    prediction = predict_default(input_values)
    
    # Display the prediction
    if prediction[0] == 1:
        st.write("Prediction: The loan will not be paid")
    else:
        st.write("Prediction: The loan will be paid")
