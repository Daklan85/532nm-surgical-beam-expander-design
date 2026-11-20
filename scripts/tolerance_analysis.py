import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. SYSTEM & THEORETICAL PARAMETERS (from Phase 2)
# ==========================================
wavelength = 532e-6  # 532 nm in mm
w0_theoretical = 0.0254  # Theoretical 1/e^2 waist radius in mm (~50.8 um diameter)
z_focus = 150.0  # Nominal focal plane distance from final objective (mm)

# Calculate theoretical Rayleigh range (z_R)
z_R = (np.pi * w0_theoretical**2) / wavelength

# Generate smooth axial positions around the focus (+/- 10 mm)
z = np.linspace(z_focus - 10.0, z_focus + 10.0, 500)

# Theoretical Gaussian beam radius w(z) and diameter 2w(z) in microns
w_z = w0_theoretical * np.sqrt(1 + ((z - z_focus) / z_R) ** 2)
diameter_theoretical_um = 2 * w_z * 1000

# Theoretical Normalized Peak Irradiance: I(z)/I0 = (w0 / w(z))^2
irradiance_norm = (w0_theoretical / w_z) ** 2

# ==========================================
# 2. OPTICSKETCHER SIMULATION DATA
# Replace these placeholder lists with your actual sensor readings!
# ==========================================
z_sim = np.array(
    [142.0, 144.0, 146.0, 148.0, 149.0, 150.0, 151.0, 152.0, 154.0, 156.0, 158.0]
)
# Example simulated 1/e^2 spot diameters (in microns) showing slight spherical aberration
diameter_sim_um = np.array(
    [110.32, 84.08, 57.84, 31.6, 18.48, 6.92, 7.76, 20.88, 47.12, 73.36, 99.58]
)

# Calculate simulated normalized irradiance relative to theoretical peak
irradiance_sim = ((2 * w0_theoretical * 1000) / diameter_sim_um) ** 2

# ==========================================
# 3. PLOTTING FOR 1080P MONITOR DISPLAY
# 16 inches x 7.5 inches at 100 DPI = 1600 x 750 pixels (fits comfortably inside 1920 x 1080)
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7.5), dpi=100)
fig.suptitle(
    "532 nm Ophthalmic Beam Delivery: Through-Focus & Tolerance Analysis",
    fontsize=15,
    fontweight="bold",
)

# --- Subplot 1: Beam Diameter vs. Axial Position ---
ax1.plot(
    z,
    diameter_theoretical_um,
    label="Theoretical Diffraction Limit",
    color="#1f77b4",
    linewidth=2.2,
)
ax1.scatter(
    z_sim,
    diameter_sim_um,
    label="OpticSketcher Ray-Trace Data",
    color="#d62728",
    zorder=5,
    s=55,
)

# Highlight Depth of Focus (DoF = 2 * z_R)
ax1.axvspan(
    z_focus - z_R,
    z_focus + z_R,
    color="#2ca02c",
    alpha=0.15,
    label=f"Depth of Focus (±{z_R:.2f} mm)",
)
ax1.axvline(z_focus, color="gray", linestyle="--", linewidth=1.2)

ax1.set_title("Beam Spot Diameter (1/e²) vs. Axial Position", fontsize=12)
ax1.set_xlabel("Axial Position from Objective Lens, z (mm)", fontsize=11)
ax1.set_ylabel("1/e² Beam Diameter (μm)", fontsize=11)
ax1.grid(True, linestyle=":", alpha=0.6)
ax1.legend(loc="upper center", fontsize=10)

# --- Subplot 2: Normalized Peak Irradiance vs. Axial Defocus ---
defocus = z - z_focus
defocus_sim = z_sim - z_focus

ax2.plot(
    defocus,
    irradiance_norm * 100,
    label="Theoretical Peak Irradiance",
    color="#1f77b4",
    linewidth=2.2,
)
ax2.scatter(
    defocus_sim,
    irradiance_sim * 100,
    label="Simulated Irradiance",
    color="#d62728",
    zorder=5,
    s=55,
)

# Highlight 50% Irradiance Threshold (Rayleigh Range boundary)
ax2.axhline(
    50,
    color="#ff7f0e",
    linestyle="--",
    linewidth=1.5,
    label="50% Irradiance Threshold (±z_R)",
)
ax2.axvspan(-z_R, z_R, color="#2ca02c", alpha=0.15)

ax2.set_title("Irradiance Roll-Off vs. Axial Defocus", fontsize=12)
ax2.set_xlabel("Axial Defocus, Δz (mm)", fontsize=11)
ax2.set_ylabel("Normalized Peak Irradiance (%)", fontsize=11)
ax2.set_ylim(0, 110)
ax2.grid(True, linestyle=":", alpha=0.6)
ax2.legend(loc="upper right", fontsize=10)

plt.tight_layout()

# Save high-resolution image (300 DPI) for GitHub/PDF report before displaying on screen
plt.savefig("through_focus_analysis.png", dpi=300, bbox_inches="tight")
plt.show()
