import streamlit as st
import pandas as pd
import joblib


model = joblib.load('best_model.pkl')

st.title("Customer Review Rating Predictor")
st.write("Predict whether a customer gives a Low, Medium or High rating.")

# Input widgets
age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
item = st.text_input("Item Purchased")
category = st.selectbox("Category", ["Clothing","Footwear","Accessories","Other"])
amount = st.number_input("Purchase Amount", min_value=0.0, value=50.0)
location = st.text_input("Location")
size = st.selectbox("Size", ["S","M","L","XL"])
color = st.text_input("Color")
season = st.selectbox("Season", ["Summer","Winter","Spring","Autumn"])
sub_status = st.selectbox("Subscription Status", ["Yes","No"])
discount = st.selectbox("Discount Applied", ["Yes","No"])
previous = st.number_input("Previous Purchases", min_value=0, value=0)
payment = st.selectbox("Payment Method", ["Card","Cash","Mobile","Other"])
frequency = st.selectbox("Frequency", ["Daily","Weekly","Monthly","Yearly"])

input_df = pd.DataFrame([{
    "Age": age,
    "Gender": gender,
    "Item Purchased": item,
    "Category": category,
    "Purchase Amount (USD)": amount,
    "Location": location,
    "Size": size,
    "Color": color,
    "Season": season,
    "Subscription Status": sub_status,
    "Discount Applied": discount,
    "Previous Purchases": previous,
    "Payment Method": payment,
    "Frequency of Purchases": frequency
}])

if st.button("Predict Rating"):
    prediction = model.predict(input_df)[0]
    rating_map = {0: 'Low', 1: 'Medium', 2: 'High'}
    st.success(f"The predicted customer rating is: {rating_map[prediction]}")

