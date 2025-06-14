# 🧠 Physics-Informed Neural Network (PINN) for Neuron Modeling

These notebooks demonstrates the use of a **Physics-Informed Neural Network (PINN)** to model the spiking behavior of a neuron based on the **Izhikevich model**. The work is part of a biomedical engineering project aimed at exploring machine learning approaches to simulate dynamic neuronal behavior.

---

## 📜 Project Summary

- **Objective:** Learn the voltage `v(t)` and recovery variable `w(t)` dynamics of a spiking neuron using PINNs.
- **Challenge:** The real neuronal signal contains rapid and irregular spikes that are difficult for a standard PINN to approximate due to its continuous-function assumption.
- **Solution:** Use a feedback mechanism from a classical numerical method (Euler's method) to guide the training and improve accuracy.

---

## ⚠️ Limitations of Pure PINN

The initial implementation trained a pure PINN without any guidance. It suffered from:

- Difficulty in learning sharp action potential spikes
- Poor convergence during training
- Inaccurate phase alignment

### 🔹 Pure PINN Output

![Pure PINN](https://github.com/MohamedBadawy19/Dynamic-Neuron-Model-Project/blob/main/results/plots/Pure_PINN_Graph.png?raw=true)

As shown above, the model failed to capture the spike morphology and timing accurately.

---

## ✅ Guided PINN with Euler Feedback

To overcome the limitations, we introduced a **feedback system** using spike detection from the Euler solution. The idea was to:

- Detect the spike times from Euler's method
- Focus training around these high-dynamic regions
- Improve convergence and accuracy using informed collocation point placement

### 🔹 Guided PINN Output

![Guided PINN](https://github.com/MohamedBadawy19/Dynamic-Neuron-Model-Project/blob/main/results/plots/PINN_vs_REF.png?raw=true)

The result shows a near-perfect match in spike timing, voltage peak, and recovery phase.

---

## 🧪 Key Features of the Notebook

- Implements Izhikevich neuron differential equations
- Trains a fully connected neural network using PyTorch
- Uses both Adam and LBFGS optimizers
- Visualizes training loss, residuals, and solution comparisons
- Compares against ground truth from Euler's method

---
