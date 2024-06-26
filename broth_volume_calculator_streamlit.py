import streamlit as st

def calculate_broth_volume(optical_density, cells_per_ml, remaining_broth_ml):
    try:
        # Constants
        desired_cells_per_ml = 500000  # 500,000 cells per ml

        # Calculation
        total_cells = cells_per_ml * remaining_broth_ml
        needed_broth_ml = (desired_cells_per_ml * remaining_broth_ml) / total_cells

        return needed_broth_ml
    except ValueError:
        return None

# Streamlit UI
st.title("Broth Volume Calculator")

optical_density = st.number_input("Optical density at 600nm:", min_value=0.0, step=0.01)
cells_per_ml = st.number_input("Cells per ml:", min_value=0.0, step=1.0)
remaining_broth_ml = st.number_input("Remaining broth (ml):", min_value=0.0, step=0.1)

if st.button("Calculate"):
    result = calculate_broth_volume(optical_density, cells_per_ml, remaining_broth_ml)
    if result is not None:
        st.success(f"Volume of broth to be added (ml): {result:.2f}")
    else:
        st.error("Please enter valid numbers.")
