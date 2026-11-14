import numpy as np

# System Parameters (in mm)
wavelength = 532e-6
d_in = 1.0
f1 = -25.0
f2 = 50.0
f3 = 150.0

# Beam Expander Calculations
mag = -f2 / f1
d_expanded = d_in * mag
lens_spacing = f1 + f2

# Focused Spot & Depth of Focus
spot_diameter = (4 * wavelength * f3) / (np.pi * d_expanded)
w0 = spot_diameter / 2
rayleigh_range = (np.pi * w0**2) / wavelength

print(f"Beam Expander Magnification: {mag:.1f}x")
print(f"Lens 1 to Lens 2 Spacing: {lens_spacing:.1f} mm")
print(f"Expanded Beam Diameter: {d_expanded:.2f} mm")
print(f"Theoretical 1/e^2 Spot Diameter: {spot_diameter * 1000:.2f} um")
print(f"Rayleigh Range (z_R): {rayleigh_range:.2f} mm")
print(f"Total Depth of Focus (2*z_R): {2 * rayleigh_range:.2f} mm")
