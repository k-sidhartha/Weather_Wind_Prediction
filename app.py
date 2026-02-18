import streamlit as st
import pickle
import pandas as pd

# Load saved pipeline model
model = pickle.load(open("final_pipeline.pkl", "rb"))

st.title("🌤 Temperature Prediction App")

precipitation = st.number_input("Precipitation", value=0.2)
temp_max = st.number_input("Max Temperature", value=32.0)
temp_min = st.number_input("Min Temperature", value=24.0)

if st.button("Predict"):

    new_data = pd.DataFrame(
        [[precipitation, temp_max, temp_min]],
        columns=['precipitation', 'temp_max', 'temp_min']
    )

    prediction = model.predict(new_data)

    st.success(f"Predicted Temperature: {prediction[0]:.2f}")
