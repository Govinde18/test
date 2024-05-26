import streamlit as st
import pandas as pd

def calculate_broth_volume(optical_density, desired_cells):
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

# Select number of samples
num_samples = st.number_input("Select number of samples:", min_value=1, max_value=15, step=1)

# Create containers for inputs
optical_density_list = []
desired_cells_list = []

# Create a table-like structure for inputs
st.subheader("Input Values")
input_columns = st.columns([1, 1])
input_columns[0].markdown("**Optical Density at 600nm**")
input_columns[1].markdown("**Desired Number of Cells**")

for i in range(num_samples):
    cols = st.columns([1, 1])
    optical_density = cols[0].number_input(f"Optical density for sample {i+1}", min_value=0.0, step=0.001, format="%.5f", key=f"od_{i}")
    desired_cells = cols[1].number_input(f"Desired cells for sample {i+1}", min_value=0.0, step=1.0, key=f"cells_{i}")
    optical_density_list.append(optical_density)
    desired_cells_list.append(desired_cells)

# Unit selection
unit = st.radio("Select the unit for the final volume:", ('Milliliters (mL)', 'Microliters (µL)'))

if st.button("Calculate"):
    results = []
    for i in range(num_samples):
        result = calculate_broth_volume(optical_density_list[i], desired_cells_list[i])
        if result is not None:
            if unit == 'Microliters (µL)':
                result *= 1000  # Convert mL to µL
                results.append({"Sample": i+1, "Volume to be added (µL)": f"{result:.4f}"})
            else:
                results.append({"Sample": i+1, "Volume to be added (mL)": f"{result:.4f}"})
        else:
            st.error(f"Please enter valid numbers for sample {i+1}.")
            results.append({"Sample": i+1, "Volume to be added": "Invalid input"})

    # Display results in a table
    results_df = pd.DataFrame(results)
    st.subheader("Results")
    st.table(results_df)
