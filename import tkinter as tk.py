import streamlit as st
import tkinter as tk
from tkinter import messagebox

def calculate_broth_volume():
    try:
        optical_density = float(entry_optical_density.get())
        cells_per_ml = float(entry_cells_per_ml.get())
        remaining_broth_ml = float(entry_remaining_broth_ml.get())

        total_cells = cells_per_ml * remaining_broth_ml
        desired_cells = 500000  # Assuming you want to achieve 500,000 cells per ml
        needed_broth_ml = (desired_cells * remaining_broth_ml) / total_cells

        result_label.config(text=f'Volume of broth to be added (ml): {needed_broth_ml:.2f}')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Broth Volume Calculator")

# Create and place the widgets
tk.Label(root, text="Optical density at 600nm:").grid(row=0, column=0, padx=10, pady=5)
entry_optical_density = tk.Entry(root)
entry_optical_density.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Cells per ml:").grid(row=1, column=0, padx=10, pady=5)
entry_cells_per_ml = tk.Entry(root)
entry_cells_per_ml.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Remaining broth (ml):").grid(row=2, column=0, padx=10, pady=5)
entry_remaining_broth_ml = tk.Entry(root)
entry_remaining_broth_ml.grid(row=2, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_broth_volume)
calculate_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()

