import streamlit as st
import requests

# 🌍 Get user country using IP
def get_country():
    try:
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        return data.get("country", "Unknown")
    except:
        return "Unknown"

# 🍽️ Food tips based on country
food_tips = {
    "US": "🇺🇸 Try grilled salmon with veggies instead of fried food.",
    "MX": "🇲🇽 Go for grilled chicken tacos with avocado and beans. Avoid creamy sauces.",
    "IN": "🇮🇳 Choose dal, grilled paneer, or tandoori instead of butter chicken daily.",
    "JP": "🇯🇵 Stick to miso soup, grilled fish, and veggie sushi. Watch soy sauce!",
    "CR": "🇨🇷 Casado with grilled chicken, black beans, and salad is a great balanced option!",
    "BR": "🇧🇷 Try feijão with veggies and lean protein. Limit fried snacks like coxinha.",
    "ES": "🇪🇸 Enjoy gazpacho, grilled fish, and legumes. Limit chorizo, fried tapas, and sugary pastries.",
    "Unknown": "🌎 Eat whole foods, fruits, veggies, lean proteins, and drink lots of water!"
}


# 🎯 App title
st.title("🌡️ BMI Calculator")

# 📥 Inputs
weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (cm):", min_value=1.0)

# 🧮 Calculate button
if st.button("Calculate BMI"):
    m2 = height / 100
    bmi = weight / (m2 ** 2)

    # 📊 BMI classification
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
        category = 'Fat 🚨'
        advice = "Talk to a health pro. Focus on balance and consistency."
        color = "red"

    # 🌍 Get country and food tip
    country = get_country()
    tip = food_tips.get(country, food_tips["Unknown"])

    # 📤 Output results
    st.markdown(f"### ✅ Your BMI is: `{bmi:.1f}`")
    st.markdown(f"**Category:** <span style='color:{color}'>{category}</span>", unsafe_allow_html=True)
    st.info(advice)

    # 📍 Show geo-based food suggestion
    st.markdown(f"---")
    st.markdown(f"📍 Based on your location **({country})**, here’s a food tip:")
    st.success(tip)
