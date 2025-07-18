# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 13:01:30 2025

@author: bhavy
"""

import pandas as pd
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/bhavy/Downloads/Deployment/trained_model.sav','rb'))

st.title("🧠 Stress Level Detection App")
st.write("Fill in the information below:")

# Inputs
gender = st.radio("Gender", ['Female', 'Male'])
gender = 1 if gender == 'Male' else 0

age = st.number_input("Age", 10, 100)

occupations = {
    'Scientist': 0, 'Doctor': 1, 'Accountant': 2, 'Teacher': 3,
    'Manager': 4, 'Engineer': 5, 'Sales Representative': 6,
    'Salesperson': 7, 'Lawyer': 8, 'Software Engineer': 9, 'Nurse': 10
}
occupation = st.selectbox("Occupation", list(occupations.keys()))
occupation = occupations[occupation]

sleep_duration = st.slider("Sleep Duration (hrs)", 0.0, 12.0, step=0.1)
quality_of_sleep = st.slider("Quality of Sleep (1-10)", 1, 10)
physical_activity_level = st.slider("Physical Activity (mins/day)", 0, 200)

bmi_category = st.radio("BMI Category", ['Underweight', 'Normal', 'Overweight'])
bmi_map = {'Underweight': 1, 'Normal': 2, 'Overweight': 3}
bmi_category = bmi_map[bmi_category]

heart_rate = st.number_input("Heart Rate (bpm)", 40, 200)
daily_steps = st.number_input("Daily Steps", 0, 30000)

sleep_disorder = st.radio("Sleep Disorder", ['Insomnia', 'Nothing', 'Sleep Apnea'])
disorder_map = {'Insomnia': 0, 'Nothing': 1, 'Sleep Apnea': 2}
sleep_disorder = disorder_map[sleep_disorder]

systolic_bp = st.number_input("Systolic Blood Pressure", 80, 200)
diastolic_bp = st.number_input("Diastolic Blood Pressure", 50, 140)

# Predict Button
if st.button("Predict Stress Level"):
    input_data = pd.DataFrame([[
        gender, age, occupation, sleep_duration, quality_of_sleep,
        physical_activity_level, bmi_category, heart_rate, daily_steps,
        sleep_disorder, systolic_bp, diastolic_bp
    ]], columns=[
        'Gender', 'Age', 'Occupation', 'Sleep Duration', 'Quality of Sleep',
        'Physical Activity Level', 'BMI Category', 'Heart Rate', 'Daily Steps',
        'Sleep Disorder', 'Systolic BP', 'Diastolic BP'
    ])
    
    prediction = loaded_model.predict(input_data)[0]
    st.success(f"🎯 Predicted Stress Level: {prediction}")
