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

# Generate input fields for each sample
for i in range(num_samples):
    st.subheader(f"Sample {i+1}")
    optical_density = st.number_input(f"Optical density at 600nm for sample {i+1} (optional):", min_value=0.0, step=0.001, format="%.5f")
    desired_cells = st.number_input(f"Desired number of cells for sample {i+1}:", min_value=0.0, step=1.0)

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
    st.table(results_df)
