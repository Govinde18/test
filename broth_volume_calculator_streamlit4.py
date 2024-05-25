import streamlit as st

def calculate_broth_volume(optical_density, cells_per_ml, desired_cells):
    try:
        # Constants
        remaining_broth_ml = 0.9

        # Calculation
        cells_per_ml = optical_density * 800000000
        total_cells = cells_per_ml * remaining_broth_ml
        needed_broth_ml = (desired_cells * remaining_broth_ml) / total_cells 

        return needed_broth_ml
    except ValueError:
        return None

# Streamlit UI
st.title("Broth Volume Calculator")

# Adding the note
st.markdown("**Note:** Optical density at 600nm value is optional. The other two are required.")

optical_density = st.number_input("Optical density at 600nm:", min_value=0.0, step=0.001)
#cells_per_ml = st.number_input("Cells per ml:", min_value=0.0, step=10.0)
desired_cells = st.number_input("Desired number of cells:", min_value=0.0, step=1.0)

# Unit selection
unit = st.radio("Select the unit for the final volume:", ('Milliliters (mL)', 'Microliters (µL)'))

if st.button("Calculate"):
    result = calculate_broth_volume(optical_density, cells_per_ml, desired_cells)
    if result is not None:
        if unit == 'Microliters (µL)':
            result *= 1000  # Convert mL to µL
            st.success(f"Volume of broth to be added (µL): {result:.4f}")
        else:
            st.success(f"Volume of broth to be added (mL): {result:.4f}")
    else:
        st.error("Please enter valid numbers.")
