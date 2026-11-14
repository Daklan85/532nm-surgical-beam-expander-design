# 532 nm Ophthalmic Laser Beam Delivery & Tolerance Analysis

## 1. Problem Statement & System Requirements
* **Application:** Retinal photocoagulation / ophthalmic surgical delivery
* **Wavelength:** 532 nm (Frequency-doubled Nd:YAG)
* **Target Working Distance:** 150 mm
* **Target Focused Spot Diameter ($1/e^2$):** ≈ 50 μm

## 2. Theoretical First-Principles Design
### 2.1 Ophthalmic Engineering Requirements
* **Laser Source Wavelength ($\lambda$):** 532 nm (Frequency-doubled Nd:YAG, $TEM_{00}$, $M^2 = 1.0$)
* **Input Collimated Beam Diameter ($D_{\text{in}}$, 1/e²):** 1.0 mm
* **Final Objective Working Distance ($f_{\text{obj}}$):** 150 mm
* **Target Focused Spot Diameter (2w₀ at 1/e²):** ≈ 50 μm
### 2.2 Beam Expansion Calculation
* Using the diffraction-limited Gaussian beam waist equation:

$$
2w_0=\frac{4\lambda f_{\text{obj}}}{\pi D_{\text{expanded}}}
$$

* Rearranging to solve for the required expanded beam diameter ($D_{\text{expanded}}$) entering the final focusing objective:

$$
D_{\text{expanded}}=\frac{4\lambda f_{\text{obj}}}{\pi (2w_0)}
$$

* Plugging in our values:

  * $\lambda = 532 \times 10^{-6}\ \text{mm}$
  * $f_{\text{obj}} = 150\ \text{mm}$
  * $2w_0 = 0.050\ \text{mm}$

$$
D_{\text{expanded}}=\frac{4 \times (532 \times 10^{-6}\ \text{mm}) \times 150\ \text{mm}}{\pi \times 0.050\ \text{mm}}\approx 2.03\ \text{mm}
$$

* Required Beam Expander Magnification:

$$
M=\frac{D_{\text{expanded}}}{D_{\text{in}}}=\frac{2.03\ \text{mm}}{1.0\ \text{mm}}\approx 2.03
$$

* **Required Magnification (M):** ≈ **2× Beam Expander**

### 2.3 Commercial-Standard Lens Selection

- **Lens 1 (Input Diverging Lens, $f_1$):** -25 mm (Plano-Concave)
- **Lens 2 (Collimating Lens, $f_2$):** +50 mm (Plano-Convex)
- **Expander Magnification ($M$):** $M = -\frac{f_2}{f_1} = -\frac{50}{-25} = 2.0\times$
- **Lens Separation ($d_{12}$):** $d_{12} = f_1 + f_2 = -25\,\text{mm} + 50\,\text{mm} = 25\,\text{mm}$
- **Lens 3 (Focusing Objective, $f_3$):** +150 mm (Plano-Convex or Achromatic Doublet, positioned 50 mm after Lens 2)

### 2.4 Calculated Depth of Focus (Rayleigh Range)

- **Rayleigh Range ($z_R$):**

$$
z_R=\frac{\pi w_0^2}{\lambda}=\frac{\pi (0.025\,\text{mm})^2}{532 \times 10^{-6}\,\text{mm}}\approx 3.69\,\text{mm}
$$

- **Total Depth of Focus ($2z_R$):**

$$
2z_R \approx 7.38\,\text{mm}
$$


## 3. Optical Layout (OpticSketcher Simulation)
* [Insert exported optical schematic from `/docs`]

## 4. Sensitivity & Tolerance Analysis
* [Axial defocus, lens tilt, and lateral decenter analysis]

## 5. Simulated Verification & Key Engineering Takeaways
* [Comparison between theoretical diffraction limit and ray-traced performance]
