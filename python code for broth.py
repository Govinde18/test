import streamlit as st

def calculate_broth_volume(optical_density, cells_per_ml, remaining_broth_ml):
  """
  Calculates the volume of broth to be added to achieve a desired cell concentration.

  Args:
      optical_density (float): Optical density at 600nm.
      cells_per_ml (float): Cells per ml in the remaining broth.
      remaining_broth_ml (float): Volume of remaining broth (ml).

  Returns:
      float: Volume of broth to be added (ml).
  """
  total_cells = cells_per_ml * remaining_broth_ml
  desired_cells = 500000  # Assuming you want to achieve 500,000 cells per ml
  needed_broth_ml = (desired_cells * remaining_broth_ml) / total_cells
  return needed_broth_ml

st.title("Broth Volume Calculator")

# Get user input
optical_density = st.number_input("Optical density at 600nm", min_value=0.0)
cells_per_ml = st.number_input("Cells per ml", min_value=0.0)
remaining_broth_ml = st.number_input("Remaining broth (ml)", min_value=0.0)

# Calculate and display results
if st.button("Calculate"):
  needed_broth_ml = calculate_broth_volume(optical_density, cells_per_ml, remaining_broth_ml)
  st.success(f"Volume of broth to be added (ml): {needed_broth_ml:.2f}")  # Format to 2 decimal places
