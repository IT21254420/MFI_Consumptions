import streamlit as st
import pandas as pd
import pickle

# Load the trained models
electricity_model = pickle.load(open('Consumptions/electricity_pkl.sav', 'rb'))
steam_model = pickle.load(open('Consumptions/steam_pkl.sav', 'rb'))
water_model = pickle.load(open('Consumptions/water_pkl.sav', 'rb'))

# Streamlit App Title
st.title("Multi-Consumption Prediction App")
st.write("")
st.write("")
st.write("")
st.markdown(
    "<div style='margin-top: 20px; font-size: 18px;'>"
    "Enter the machine parameters below to predict Electricity, Steam, and Water Consumption."
    "</div>",
    unsafe_allow_html=True,
)

st.write("")  # Add an empty line for spacing
st.write("")
st.write("")
st.write("")

# Create two columns for input layout
col1, col2 = st.columns(2)

# Inputs for the left column
with col1:
    knitting = st.number_input("Number of Knitting Machines", min_value=0, value=None, step=1, format="%d")
    bulk_dye = st.number_input("Number of Bulk Dye Machines", min_value=0, value=None, step=1, format="%d")
    sample_dye = st.number_input("Number of Sample Dye Machines", min_value=0, value=None, step=1, format="%d")
    dryers = st.number_input("Number of Dryers", min_value=0, value=None, step=1, format="%d")
    presetting = st.number_input("Number of Presetting Machines", min_value=0, value=None, step=1, format="%d")

# Inputs for the right column
with col2:
    chillers = st.number_input("Number of Chillers", min_value=0, value=None, step=1, format="%d")
    ahu = st.number_input("Number of AHU Machines", min_value=0, value=None, step=1, format="%d")
    compressor = st.number_input("Number of Compressors", min_value=0, value=None, step=1, format="%d")
    luwa = st.number_input("Number of Luwa Machines", min_value=0, value=None, step=1, format="%d")

st.write("")
st.write("")
st.write("")

# Prediction Button
if st.button("Predict Consumption"):
    # Check if all inputs are provided
    if None in [knitting, bulk_dye, sample_dye, dryers, presetting, chillers, ahu, compressor, luwa]:
        st.error("Please fill in all the fields before predicting.")
    else:
        # Create a DataFrame for input
        input_data = {
            'Knitting': [knitting],
            'Bulk_Dye': [bulk_dye],
            'Sample_Dye': [sample_dye],
            'Dryers': [dryers],
            'Presetting': [presetting],
            'Chillers': [chillers],
            'AHU': [ahu],
            'Compressor': [compressor],
            'Luwa': [luwa]
        }
        input_df = pd.DataFrame(input_data)
        
        # Predict using the models
        electricity_pred = electricity_model.predict(input_df)
        steam_pred = steam_model.predict(input_df)
        water_pred = water_model.predict(input_df)
        
        # Display Predictions
        st.write("")
        st.write("")
        st.write("")
        st.subheader("Predicted Consumption Results")
        st.write("")
        st.write(f"**Electricity Consumption (kWh):** {electricity_pred[0]:.2f}")
        st.write(f"**Steam Consumption (kg):** {steam_pred[0]:.2f}")
        st.write(f"**Water Consumption (Cu.m.):** {water_pred[0]:.2f}")
