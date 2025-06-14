# Backward Euler Simulation of Izhikevich Neuron Model  
**Author:** Alaa Essam  
**Project:** Computational Neuroscience Neural Modeling  
**Tool Used:** Python (NumPy, Matplotlib)  

## Overview  
This project implements the **Izhikevich neuron model** using the **Backward Euler method** (an implicit numerical integration technique).  
The purpose is to explore how this implicit method improves stability in stiff systems—common in biological neuron models with fast dynamics.

## Why Backward Euler?  
- Handles **stiff ODEs** that occur in neural modeling (like ion channel dynamics).  
- Offers **numerical stability** even with larger time steps.  
- Better suited for **long-term simulations** of neural behavior.

## Core Idea (Math Explanation)  
- **Forward Euler:**  
  `Yn+1 = Yn + h * f(tn, Yn)`  
  (uses known info to predict the next state)

- **Backward Euler:**  
  `Yn+1 = Yn + h * f(tn+1, Yn+1)`  
  (requires solving for the next state — more stable but more complex)

In this model, we solve this nonlinear system using **Newton’s method** at each time step.

## What I Did  
- Coded the **Izhikevich model** using Backward Euler with Newton iteration.  
- Simulated the **membrane potential (v)** and **recovery variable (w)** over time.  
- Detected and logged **spikes** and **iteration convergence behavior**.  
- Visualized:  
  - Voltage vs. Time  
  - Recovery Variable vs. Time  
  - Phase plane (w vs. v)  
  - Zoomed-in phase plane  
- Printed iteration diagnostics for the first few steps.  
- Summarized results: min/max voltage and spike count.

## Parameters Used  
- `C = 100`, `vr = -60`, `vt = -40`, `k = 0.7`  
- `a = 0.03`, `b = -2`, `c = -50`, `d = 20`, `vpeak = 35`  
- Constant input current `I = 100`  
- Time range: 1000 ms, step size: 0.25 ms

## What the Output Shows  
- **Voltage spikes** at regular intervals  
- **Recovery variable** adjusting after each spike  
- **Stable numerical behavior** over long simulation  
- Number of spikes, and how often Newton iteration converges

## When to Use This Method  
✅ When equations are stiff or change very fast  
✅ When stability is more important than speed  
✅ In biologically accurate neural modeling

## When Not to Use  
❌ If the system is simple (use Forward Euler instead)  
❌ If computational speed is a priority  
❌ If writing simple, fast code is the goal

## How to Run  
1. Install dependencies:  
```bash
pip install numpy matplotlib
