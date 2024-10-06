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
    
    st.write("""
    This app calculates the transformation efficiency using the formula:
    
    \[
    TE = \frac{{\text{{colonies}} \times \text{{recovery volume (mL)}}}}{{\text{{DNA added (µg)}} \times \text{{volume plated (mL)}}}}
    \]
    
    **Transformation Efficiency** is measured in colonies per microgram of DNA (**colonies/µg DNA**).
    """)
    
    # Input fields
    colonies = st.number_input('Total colonies on the plate', min_value=1, value=1, step=1)
    recovery_volume_ml = st.number_input('Final volume after recovery (in mL)', min_value=0.0, value=1.0, format="%.2f")
    dna_ug = st.number_input('Amount of DNA added (in µg)', min_value=0.0, value=0.01, format="%.2f")
    volume_plated_ml = st.number_input('Volume plated (in mL)', min_value=0.0, value=0.1, format="%.2f")
    
    # Calculate button
    if st.button('Calculate'):
        try:
            te = calculate_transformation_efficiency(colonies, recovery_volume_ml, dna_ug, volume_plated_ml)
            st.success(f"Transformation efficiency: {te:.2e} colonies/µg DNA")
        except ValueError as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
