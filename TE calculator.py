import streamlit as st

def calculate_transformation_efficiency(colonies, recovery_volume_ml, dna_ug, volume_plated_ml):
    """Calculate transformation efficiency."""
    if dna_ug <= 0 or volume_plated_ml <= 0:
        raise ValueError("DNA amount and volume plated must be greater than zero.")
    
    # Formula: (Number of colonies * final recovery volume) / (DNA (µg) * Volume plated)
    transformation_efficiency = (colonies * recovery_volume_ml) / (dna_ug * volume_plated_ml)
    return transformation_efficiency

def main():
    st.title("Transformation Efficiency Calculator")
    
    # Input fields for user data
    colonies = st.number_input('Total colonies on the plate:', min_value=0, value=0)
    recovery_volume_ml = st.number_input('Final volume after recovery (in mL):', min_value=0.0, value=1.0)
    dna_ug = st.number_input('Amount of DNA added (in µg):', min_value=0.0, value=0.1)
    volume_plated_ml = st.number_input('Volume plated (in mL):', min_value=0.0, value=0.1)
    
    # Calculate transformation efficiency when button is clicked
    if st.button('Calculate'):
        try:
            te = calculate_transformation_efficiency(colonies, recovery_volume_ml, dna_ug, volume_plated_ml)
            st.success(f"Transformation efficiency: {te:.2e} colonies/µg DNA")
        except ValueError as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
