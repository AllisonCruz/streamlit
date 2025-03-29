import streamlit as st

st.title("🌡️ BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (cm):", min_value=1.0)

if st.button("Calculate BMI"):
    m2 = height / 100
    bmi = weight / (m2 ** 2)

    if bmi < 18.5:
        category = 'Underweight 🦴'
        advice = "Eat nutrient-rich foods and try strength training."
        color = "cyan"
    elif bmi < 24.9:
        category = 'Normal 💪'
        advice = "Great job! Keep eating healthy and exercising."
        color = "green"
    elif bmi < 29.9:
        category = 'Overweight 🍔'
        advice = "Add whole foods and stay active daily."
        color = "orange"
    else:
        category = 'Obesity 🚨'
        advice = "Talk to a health pro. Focus on balance and consistency."
        color = "red"

    st.markdown(f"### ✅ Your BMI is: `{bmi:.1f}`")
    st.markdown(f"**Category:** <span style='color:{color}'>{category}</span>", unsafe_allow_html=True)
    st.info(advice)
