# Neural Modeling with RKC Method  
### Alaa Essam’s Report  

---

## 🧠 Project Title:
**The future depends on smooth and stable jumps — with extra help from Chebyshev's math magic**

---

## 📌 Objective:

This project aims to simulate the Izhikevich neuron model using an **explicit stabilized method** called **RKC (Runge-Kutta-Chebyshev)** instead of the classical Euler or Backward Euler methods. The goal is to handle **stiff neural dynamics** more efficiently and stably, without requiring tiny time steps.

---

##⚙️ Background: Why RKC?

In neural modeling, especially with ion channels, we often face **stiff systems** — where voltage and current can change very rapidly. Using traditional methods like:
- **Euler:** Unstable for stiff systems.
- **Backward Euler:** Stable but **implicit** (requires solving equations).

💡 **RKC bridges the gap**:
- Allows **larger time steps**.
- Is **explicit**, so it's easier to implement.
- Uses **Chebyshev polynomial constants** to improve stability.

---

## 🧮 Mathematical Idea (Simplified):

RKC does not fully rely on the **present** (like Euler), nor does it guess the **future** (like Backward Euler).  
It builds the next step using **tiny sub-steps**, each weighted using **Chebyshev constants** for better stability.

### 2-Stage RKC Formula:
Y₀ = Yₙ
Y₁ = Y₀ + μ₁·h·f(tₙ, Y₀)
Y₂ = (1−a₁)·Y₀ + a₁·Y₁ + μ₂·h·f(tₙ + c₂·h, Y₁)


Where:
- Y₀: current state
- Y₂: next step
- μ₁, μ₂, a₁, c₂: Chebyshev-based constants

---

## 🧪 Simulation Details:

- **Model:** Izhikevich neuron
- **Method used:** RKC solver with Chebyshev-stabilized steps
- **Programming Language:** Python
- **Duration:** 20 ms
- **Time Step (dt):** 0.25 ms
- **Stages:** 4
- **Spike Threshold:** 35 mV

---

## 🧾 Code Highlights:

- Simulation uses `rkc_solver()` to integrate over time.
- Includes **spike detection and reset mechanism**.
- Tracks and prints details per iteration.
- Visualizes:
  - Membrane potential over time
  - Recovery variable
  - Phase plane (w vs v)
  - Zoomed phase plane

---

## 📊 Output Snapshots:
- Printed output shows the first 50 iteration steps (v, w before & after, with messages).
- Final plots are generated using **matplotlib** for better visualization.
- Summary includes:
  - Maximum & minimum voltage
  - Spike count

---

## ✅ Why Use RKC?

1. Stable for stiff systems (ideal for neurons with fast dynamics)
2. Allows larger time steps → faster simulation
3. Explicit method → easier to implement than backward/implicit methods

---

## ⚠️ Limitations of RKC:

1. Not efficient for non-stiff ODEs
2. Needs careful parameter tuning
3. Works only for explicit ODEs
4. Not ideal for fast nonlinear shifts
5. Can be slow for long simulations
6. Not commonly supported in basic ODE libraries

---

## 📌 Summary:

This project demonstrates how the **Runge-Kutta-Chebyshev method** can enhance the stability and performance of neural simulations. By leveraging mathematical stability from Chebyshev polynomials, we successfully captured **neural spikes** and **voltage dynamics** in a realistic way — without the burden of implicit computation.

---

## 🧠 Author:
**Alaa Essam**  
Faculty of Engineering, Cairo University  
Project on Computational Neuroscience  
