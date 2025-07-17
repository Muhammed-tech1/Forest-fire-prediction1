import streamlit as st
import pandas as pd 
import joblib

model = joblib.load("forest_fire.joblib")
st.set_page_config(page_title="Forest Fire Prediction", layout="centered")

# Add background image using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("🌲 Forest Fire Prediction App")
st.write("Enter environmental and time-based conditions below to check fire risk.")

# Input form
with st.form("fire_form"):
    DAY = st.number_input("Day", min_value=1, max_value=31)
    MONTH = st.number_input("Month", min_value=1, max_value=12)
    YEAR = st.number_input("Year", min_value=1990, max_value=2100)
    TEMPERATURE = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1)
    RH = st.number_input("Relative Humidity (%)", min_value=0.0, max_value=100.0, step=0.5)
    WS = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=100.0, step=0.5)
    FFMC = st.number_input("FFMC", min_value=0.0, max_value=150.0)
    DMC = st.number_input("DMC", min_value=0.0, max_value=300.0)
    DC = st.number_input("DC", min_value=0.0, max_value=1000.0)
    RAIN = st.number_input("Rain", min_value=0.0, max_value=0.182265)
    ISI = st.number_input("ISI", min_value=0.0, max_value=100.0)
    BUI = st.number_input("BUI", min_value=0.0, max_value=300.0)
    FWI = st.number_input("FWI", min_value=0.0, max_value=100.0)
    REGION = st.selectbox("Region", [0, 1])  #  0 = Bejaia, 1 = Sidi-Bel Abbes

    submitted = st.form_submit_button("Predict Fire Risk")

if submitted:
    # Prepare input
    input_df = pd.DataFrame([{
        "DAY": DAY,
        "MONTH": MONTH,
        "YEAR": YEAR,
        "TEMPERATURE": TEMPERATURE,
        "RH": RH,
        "WS": WS,
        "FFMC": FFMC,
        "DMC": DMC,
        "DC": DC,
        "RAIN": RAIN,
        "ISI": ISI,
        "BUI": BUI,
        "FWI": FWI,
        "REGION": REGION
    }])

    # Predict
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("🔥 High Risk: Forest Fire Likely!")
    else:
        st.success("✅ Low Risk: No Fire Predicted.")

 