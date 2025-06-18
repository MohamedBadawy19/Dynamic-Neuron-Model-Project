# 🧠 Explicit Euler Method for Neuron Simulation

This project implements the **Explicit Euler Method** to simulate a dynamic neuron model using a system of ordinary differential equations (ODEs). It's a simple yet powerful numerical technique suitable for initial testing and exploration.

---

## 📘 Model Description

The neuron is described by the following coupled ODEs:

$\[
\frac{dv}{dt} = \frac{k(v - v_r)(v - v_t) - w + I_n}{C}
\]$

$\[
\frac{dw}{dt} = a[b(v - v_r) - w]
\]$

### Parameters

| Parameter | Description | Value |
|----------|-------------|-------|
| `C` | Membrane capacitance | 100 |
| `v_r` | Resting membrane potential | -60 mV |
| `v_t` | Threshold potential | -40 mV |
| `v_peak` | Spike threshold | 35 mV |
| `k` | Scaling constant | 0.7 |
| `a` | Recovery time constant | 0.03 |
| `b` | Recovery sensitivity | -2 |
| `I_n` | Input current | 0 (t < 101), 70 (t ≥ 101) |
| `h` | Step size | 1 ms |

---

## ⚙️ Simulation Flow

1. Initialize parameters and starting values:  
   $\[
   v(0) = -60, \quad w(0) = 0
   \]$

2. Use Euler’s formula:
   $\[
   y[i+1] = y[i] + h \cdot f(t_i, y[i])
   \]$

3. Reset condition (when spike is detected):  
   $\[
   v = -50, \quad w = w + 100
   \]$

4. Plot results:
   - Membrane potential over time
   - Recovery variable over time
   - Phase-plane plot (w vs. v)

---

## 📊 Sample Plots

> ✅ Auto-generated:
- `v(t)` (Membrane Potential)
- `w(t)` (Recovery Variable)
- Phase Plane (`w vs. v`)

---

## 🧪 Example Output
Elapsed time: 5.57 ms
t = 0.0: v = -60.0000, w = 0.0000
t = 250.0: v = ..., w = ...
...
---
## 📦 Requirements

```bash
pip install numpy matplotlib
```
---
▶️ How to Run
```bash
python euler_neuron_simulation.py
```
---
✅ Advantages
- Simple and intuitive

- Fast per-step computation

- Great for initial testing and concept validation

❌ Limitations
- Low accuracy (first-order method)

- Unsuitable for stiff or rapidly changing systems
