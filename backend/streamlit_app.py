# streamlit_app.py
import streamlit as st
import pandas as pd
import pickle

# Load model and scalers
model = pickle.load(open('models/random_forest.pkl', 'rb'))
sc = pickle.load(open('models/input_scaler.pkl', 'rb'))
sct = pickle.load(open('models/output_scaler.pkl', 'rb'))

model = pickle.load(open('models/random_forest.pkl', 'rb'))
sc = pickle.load(open('models/input_scaler.pkl', 'rb'))
sct = pickle.load(open('models/output_scaler.pkl', 'rb'))


st.title("Medical Insurance Cost Predictor")

age = st.number_input("Age", 18, 100, 30)
sex = st.selectbox("Sex", ['Male', 'Female'])
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.number_input("Children", 0, 10, 0)
smoker = st.selectbox("Smoker", ['Yes', 'No'])
region = st.selectbox("Region", ['southeast', 'southwest', 'northeast', 'northwest'])

# Convert categorical to encoded
sex = 1 if sex == 'Male' else 0
smoker = 1 if smoker == 'Yes' else 0
region_map = {'northeast': 0, 'northwest': 1, 'southeast': 2, 'southwest': 3}
region = region_map[region]

# Feature Engineering
data = {
    'age': age,
    'sex': sex,
    'bmi': bmi,
    'children': children,
    'smoker': smoker,
    'region': region,
    'age_bmi': age * bmi,
    'bmi_squared': bmi ** 2,
    'age_smoker': age * smoker,
    'bmi_smoker': bmi * smoker,
    'age_bmi_smoker': age * bmi * smoker
}
df = pd.DataFrame([data])
df_scaled = df.copy()
cols_to_scale = ['age','bmi','age_bmi','bmi_squared','age_smoker','bmi_smoker','age_bmi_smoker']
df_scaled[cols_to_scale] = sc.transform(df_scaled[cols_to_scale])

# Prediction
if st.button("Predict"):
    pred = model.predict(df_scaled)
    final = sct.inverse_transform(pred.reshape(-1,1))
    st.success(f"Estimated Insurance Cost: ₹{final[0][0]:,.2f}")
