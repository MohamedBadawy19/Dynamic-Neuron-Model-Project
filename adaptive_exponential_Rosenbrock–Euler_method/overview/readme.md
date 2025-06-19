# Adaptive Exponential Rosenbrock–Euler Method (ExpRESS–Euler)

This project presents a detailed implementation and analysis of the **Adaptive Exponential Rosenbrock–Euler Method (ExpRESS–Euler)**, a numerical scheme designed to solve stiff ordinary differential equations (ODEs) efficiently. It is particularly suited for neuron models where abrupt state changes and nonlinear dynamics often lead to stiffness.

---

## 📋 Contents Overview

The report includes the following:

### ✅ 1. ODE System
Describes the two coupled differential equations modeling a neuron's membrane potential `v` and recovery variable `w`:
'''
dv/dt = k(v − vr)(v − vt) − w + In
dw/dt = a[b(v − vr) − w]
'''

### ✅ 2. Parameters & Initial Conditions
A breakdown of all parameters, constants, and initial values used in the simulation, including:
- Membrane capacitance `C`
- Resting & threshold potentials (`vr`, `vt`)
- Input current `In`
- Recovery sensitivity `a`, `b`
- Reset mechanism when `v ≥ v_peak`

### ✅ 3. Methodology: ExpRESS–Euler
A step-by-step explanation of the ExpRESS–Euler method:
- Adaptive step-size control
- Use of Jacobian `Jn` (∂f/∂y)
- Matrix exponential function φ₁(h·J)
- Local error estimation via two-step method
- Time-step adaptation logic:  
  `h_new = h * (tol / error)^0.5`

### ✅ 4. Python Implementation
Code that:
- Solves the ODE system using ExpRESS–Euler
- Visualizes `v` and `w` over time
- Plots phase space (`w` vs `v`)

### ✅ 5. Results & Error Analysis
A table comparing the ExpRESS–Euler output with reference values from the Explicit Euler method:
- Tracks error in `v` and `w` at key time points
- Error percentages included for interpretability

### ✅ 6. Pros and Cons
**Pros:**
- Strong handling of stiff systems
- Adaptive time-stepping increases efficiency
- Numerically stable with larger step sizes

**Cons:**
- Jacobian computation adds complexity
- First-order accurate only
- Implementation is less intuitive than standard methods (Euler, RK)

---

## 📊 Sample Output

| Time (ms) | v_sim  | v_ref  | v_err | v_err % | w_sim | w_ref  | w_err | w_err % |
|----------:|--------|--------|-------|---------|-------|--------|-------|---------|
| 0.0       | -60.00 | -60.00 | 0.00  | 0.00%   | 0.000 | 0.000  | 0.000 | —       |
| 250.0     | -55.01 | -54.48 | 0.53  | 0.97%   | 5.950 | 6.283  | 0.333 | 5.31%   |
| 500.0     | -51.00 | -50.62 | 0.38  | 0.76%   | 60.00 | 59.09  | 0.909 | 1.54%   |
| 750.0     | -50.00 | -49.55 | 0.45  | 0.90%   | -13.0 | -12.48 | 0.524 | 4.20%   |
| 1000.0    | -54.00 | -53.70 | 0.30  | 0.56%   | 2.000 | 1.565  | 0.435 | 27.80%  |

---

## 💡 Purpose

This report serves both as:
- A demonstration of an advanced numerical technique in neuroscience modeling.
- A benchmark for comparing solver performance on stiff ODEs.

