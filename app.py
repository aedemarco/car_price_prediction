import streamlit as st
import pandas as pd
import joblib

# --------------------
# Load model & metadata
# --------------------
model = joblib.load("car_price_model.pkl")
metadata = joblib.load("metadata.pkl")

categorical_cols = metadata["categorical_cols"]
numerical_cols = metadata["numerical_cols"]

# --------------------
# Streamlit UI
# --------------------
st.set_page_config(page_title="Car Price Predictor", layout="centered")
st.title("🚗 Car Price Prediction App")

st.write("Select car attributes and click **Predict** to estimate the car price.")

# Create input widgets for categorical features
inputs = {}
for col in categorical_cols:
    # Extract categories from model’s OneHotEncoder
    try:
        categories = model.named_steps["preprocessor"].transformers_[1][1].categories_
        cat_dict = dict(zip(categorical_cols, categories))
        options = cat_dict[col]
    except Exception:
        options = []
    
    if len(options) > 0:
        inputs[col] = st.selectbox(f"{col}", options)
    else:
        inputs[col] = st.text_input(f"{col}")

# Create sliders for numerical features
# (using generic ranges since we don't have raw df here)
for col in numerical_cols:
    if col == "Horsepower":
        inputs[col] = st.slider(f"{col}", 40, 300, 150)
    elif col == "EngineSize":
        inputs[col] = st.slider(f"{col}", 1.0, 6.0, 3.0, step=0.1)
    else:
        # fallback generic range
        inputs[col] = st.number_input(f"{col}", value=0.0)

# --------------------
# Prediction
# --------------------
if st.button("🔮 Predict Price"):
    user_input_df = pd.DataFrame([inputs])
    predicted_price = model.predict(user_input_df)[0]
    st.success(f"💰 Estimated Price: **${predicted_price:,.2f}**")
