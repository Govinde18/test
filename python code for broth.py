import streamlit as st

def calculate_broth_volume(optical_density, cells_per_ml, remaining_broth_ml):
    total_cells = cells_per_ml * remaining_broth_ml
    desired_cells = 500000  # Assuming you want to achieve 500,000 cells per ml
    needed_broth_ml = (desired_cells * remaining_broth_ml) / total_cells
    return needed_broth_ml

st.title("Broth Volume Calculator")

# Input fields
optical_density = st.number_input('Optical density at 600nm:', min_value=0.0, step=0.01)
cells_per_ml = st.number_input('Cells per ml:', min_value=0.0, step=0.01)
remaining_broth_ml = st.number_input('Remaining broth (ml):', min_value=0.0, step=0.01)

# Calculate button
if st.button('Calculate'):
    if cells_per_ml > 0 and remaining_broth_ml > 0:
        needed_broth_ml = calculate_broth_volume(optical_density, cells_per_ml, remaining_broth_ml)
        st.success(f'Volume of broth to be added (ml): {needed_broth_ml:.2f}')
    else:
        st.error("Please enter values greater than 0 for cells per ml and remaining broth.")
