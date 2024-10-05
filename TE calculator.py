import streamlit as st

def calculate_transformation_efficiency(colonies, recovery_volume_ml, dna_ug, volume_plated_ml):
    # Formula to calculate transformation efficiency
    transformation_efficiency = (colonies * recovery_volume_ml) / (dna_ug * volume_plated_ml)
    return transformation_efficiency

# Streamlit app
st.title("Transformation Efficiency Calculator")

# User input fields
colonies = st.number_input('Total colonies on the plate', min_value=1, value=1, step=1)
recovery_volume_ml = st.number_input('Final volume after recovery (in mL)', min_value=0.0, value=1.0, format="%.2f")
dna_ug = st.number_input('Amount of DNA added (in µg)', min_value=0.0, value=0.01, format="%.2f")
volume_plated_ml = st.number_input('Volume plated (in mL)', min_value=0.0, value=0.1, format="%.2f")

# Button to trigger the calculation
if st.button('Calculate'):
    if dna_ug == 0 or volume_plated_ml == 0:
        st.error('DNA amount and volume plated must be greater than zero')
    else:
        # Calculate transformation efficiency
        te = calculate_transformation_efficiency(colonies, recovery_volume_ml, dna_ug, volume_plated_ml)
        st.success(f"Transformation efficiency: {te:.2e} colonies/µg DNA")

