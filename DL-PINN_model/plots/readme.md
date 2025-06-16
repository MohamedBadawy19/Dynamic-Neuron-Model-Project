## 📊 Results and Visualizations

### 🔹 Reference: Euler’s Method Results
These plots represent the membrane potential and recovery variable as simulated using **Euler's Method**. They serve as a reference to evaluate the accuracy of the PINN model.

- **Membrane Potential (v):**

  ![Membrane Potential Plot](https://github.com/MohamedBadawy19/Dynamic-Neuron-Model-Project/blob/main/results/plots/V_Euler.png?raw=true)

- **Recovery Variable (w):**

<img src="https://raw.githubusercontent.com/MohamedBadawy19/Dynamic-Neuron-Model-Project/main/results/plots/W_Euler.png" alt="Recovery Variable Plot" width="500"/>

---

### 🔹 Initial PINN Training (160 ms)

We first trained the PINN model over a 160 ms window. However, the performance was poor due to its inability to capture rapid voltage spikes.

- **Initial PINN Output (160 ms):**

  ![Initial Result Plot](https://github.com/MohamedBadawy19/Dynamic-Neuron-Model-Project/blob/main/results/plots/PINN160.png?raw=true)

---

### 🔹 Improved PINN Using Spike Detection

To improve the results, we implemented a spike-detection mechanism that allowed the model to better learn the sharp transitions in the neuron signal. This yielded a significantly more accurate outcome.

- **Final PINN vs. Reference:**

  ![Final Result Plot](https://github.com/MohamedBadawy19/Dynamic-Neuron-Model-Project/blob/main/results/plots/PINN_vs_REF.png?raw=true)

- **Phase Space Plot (v-w):**

  ![Phase Plot](https://github.com/MohamedBadawy19/Dynamic-Neuron-Model-Project/blob/main/results/plots/PhaseGraph.png?raw=true)

- **Error Over Time (%):**

  ![Error Plot](https://github.com/MohamedBadawy19/Dynamic-Neuron-Model-Project/blob/main/results/plots/ErrorOverTime.png?raw=true)

- **Residuals Across Domain:**

  ![Residuals Plot](https://github.com/MohamedBadawy19/Dynamic-Neuron-Model-Project/blob/main/results/plots/Residuals.png?raw=true)

- **Training Loss Curve:**

  ![Training Loss Plot](https://github.com/MohamedBadawy19/Dynamic-Neuron-Model-Project/blob/main/results/plots/TrainingLoss.png?raw=true)
