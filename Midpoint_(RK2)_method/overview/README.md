
# 🧠 Midpoint (RK2) Method for Izhikevich Neuron Model

A Python implementation of the Midpoint Method (Runge-Kutta 2) to solve the Izhikevich spiking neuron model. 
This project demonstrates how to numerically simulate neuron behavior and visualize the results.

## 📌 Overview

The Izhikevich model simulates spiking neuron behavior using two coupled differential equations. 
These are often **stiff ODEs**, requiring careful numerical methods for stable and accurate simulation.

This implementation uses the **Midpoint (RK2) method** to solve the following equations:

```
C * dv/dt = k * (v - vr) * (v - vt) - w + I_in
dw/dt     = a * (b * (v - vr) - w)
```
## 🧪 Parameters

| Parameter | Description                        | Value    |
|-----------|------------------------------------|----------|
| C         | Capacitance                        | 100      |
| k         | Voltage scaling factor             | 0.7      |
| vr        | Resting potential                  | -60      |
| vt        | Threshold potential                | -40      |
| a         | Recovery speed                     | 0.03     |
| b         | Coupling of v to w                 | -2       |
| d         | Increment to w after spike         | 100      |
| V_peak    | Spike threshold                    | 35       |
| v0        | Initial membrane potential         | -60      |
| w0        | Initial recovery variable          | 0        |
| I_in      | Input current (0 if t<101ms else 70)| 0 or 70  |


## 🧮 Midpoint (RK2) Method Equations

We are solving the Izhikevich model using the Midpoint (RK2) method:

Steps of the RK2 method:

1.  K1v = (1/C) * [k * (v - vr) * (v - vt) - w + I_in]
2.  K1w = a * [b * (v - vr) - w]

3.  v_mid = v + (h / 2) * K1v
4.  w_mid = w + (h / 2) * K1w

5.  K2v = (1/C) * [k * (v_mid - vr) * (v_mid - vt) - w_mid + I_in]
6.  K2w = a * [b * (v_mid - vr) - w_mid]

7.  v_next = v + h * K2v
8.  w_next = w + h * K2w

Spike reset condition:
If v_next >= V_peak :
-  v_next = c  (typically -50)
-  w_next += d


## ⚙️ Midpoint (RK2) Method Steps

1. Compute K1 values from current `v` and `w`
2. Estimate midpoint values `v_mid` and `w_mid`
3. Compute K2 values using the midpoint estimates
4. Update `v` and `w` for the next step

If `v` exceeds `V_peak`, it is reset to -50 and `w` is incremented by `d`.

## 🚀 How to Run

```bash
pip install numpy pandas matplotlib
python Midpoint(Rk2).py
```


## 📊 Output

- Time series of membrane potential `v` and recovery variable `w`
- Phase plot (`v` vs `w`)
- Dataframe of intermediate values (K1, K2, etc.)

## ✅ Advantages

- Easy to implement in Python
- More accurate than Euler for the same step size
- Less computationally expensive than RK4

## ⚠️ Limitations

- Less accurate than RK4
- More expensive than Euler
- Not ideal for stiff ODEs without very small step size

## 📄 License
MIT License.

## Author
© 2025 Omar Gamal @OmarGamalH
