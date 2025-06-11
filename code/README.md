# Dynamic Neuron Model with PINN and Numerical Methods

This project implements and compares different approaches for solving the **Dynamic Neuron Model (DNM)** ODE system from Schiesser's textbook:

> *Schiesser, W.E. (2014). Dynamic Neuron Models in Biomedical Engineering (Chapter 4).*

We use:
- 🧮 **Numerical methods**: Euler and RK4
- 🧠 **Physics-Informed Neural Networks (PINNs)**

---

## 📌 Problem Description

The DNM describes a neuron’s membrane voltage `v(t)` and a recovery variable `w(t)` using a system of ODEs:

C dv/dt = k(v - vr)(v - vt) - w + In(t)
dw/dt = a[b(v - vr) - w]

yaml
Copy
Edit

with spike-reset conditions:
- If `v ≥ v_peak`:  
  `v ← c`,  
  `w ← w + d`

This system simulates neuron spikes in response to an external current `In(t)`.

---

## 🛠️ What’s Included

- `PINN_Model.ipynb`: Main Python script with:
  - Euler and RK4 solvers
  - Physics-Informed Neural Network (PINN) on `[0, 200 ms]`
  - Full plots and comparisons
- `README.md`: This file

---

## 🧠 Why Use PINNs?

- Traditional solvers (Euler, RK4) require discretization.
- **PINNs** learn a continuous function that obeys the differential equations, using only the **physics (ODEs)** — no training data required.
- Great for inverse problems, learning dynamics from sparse data, or continuous generalization.

---

## 📊 Results

- The PINN learns accurate membrane dynamics on `[0–200 ms]` before the first spike.
- It matches RK4 with high accuracy (MSE < `1e-3`).
- Euler and RK4 show full spike trains up to 1000 ms, confirming correctness.

---

## 🧪 Parameters Used

From the reference textbook (Ch.4):

| Parameter | Value     | Description                    |
|-----------|-----------|--------------------------------|
| C         | 100       | Capacitance                    |
| vr        | -60       | Resting potential              |
| vt        | -40       | Threshold potential            |
| k         | 0.7       | Spike steepness                |
| a         | 0.03      | Recovery time constant         |
| b         | -2        | Recovery sensitivity           |
| c         | -50       | Reset voltage after spike      |
| d         | 100       | Recovery increment after spike |
| v_peak    | 35        | Spike threshold (cutoff)       |
| In(t)     | 0 → 70    | Step current at t = 100 ms     |

---

## ⚠️ Limitations

- PINNs struggle to learn sharp discontinuities like spike resets.
- This implementation only trains the PINN on **[0, 200 ms]** to avoid discontinuities.
- For full spike learning, future work can:
  - Train PINNs segment-wise
  - Encode reset logic directly into the network or loss
