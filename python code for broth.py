# Calculate the volume of broth to be added

# Inputs
optical_density = float(input('Optical density at 600nm: '))
cells_per_ml = float(input('Cells per ml: '))
remaining_broth_ml = float(input('Remaining broth (ml): '))

# Calculation
total_cells = cells_per_ml * remaining_broth_ml
desired_cells = 500000  # Assuming you want to achieve 500,000 cells per ml
needed_broth_ml = (desired_cells * remaining_broth_ml) / total_cells

# Output the volume of broth to be added
print('Volume of broth to be added (ml):', needed_broth_ml)