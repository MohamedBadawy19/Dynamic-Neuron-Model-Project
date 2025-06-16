## 📊 Results and Visualizations

### 🔹 Reference: Euler’s Method Results
These plots represent the membrane potential and recovery variable as simulated using **Euler's Method**. They serve as a reference to evaluate the accuracy of the PINN model.

- **Membrane Potential (v):**

![V_Euler](https://github.com/user-attachments/assets/26bb247d-f1bc-44e7-bf3a-c0e1f5b85525)

- **Recovery Variable (w):**

![W_Euler](https://github.com/user-attachments/assets/b3e1ed06-7e6d-4fe0-992f-8aea3f1a9395)

---

### 🔹 Initial PINN Training (160 ms)

We first trained the PINN model over a 160 ms window. However, the performance was poor due to its inability to capture rapid voltage spikes.

- **Initial PINN Output (160 ms):**
      ![PINN160](https://github.com/user-attachments/assets/9523300f-8393-4233-bff1-678ee131de35)
  
---

### 🔹 Improved PINN Using Spike Detection

To improve the results, we implemented a spike-detection mechanism that allowed the model to better learn the sharp transitions in the neuron signal. This yielded a significantly more accurate outcome.

- **Final PINN vs. Reference:**
  
    ![PINN_vs_REF](https://github.com/user-attachments/assets/f705944b-3426-4b52-8990-1613d470a33e)

- **Phase Space Plot (v-w):**

    ![PhaseGraph](https://github.com/user-attachments/assets/5f6c9191-c11a-4b20-98a2-608f2696201c)

- **Error Over Time (%):**
  
  ![ErrorOverTime](https://github.com/user-attachments/assets/4996b7e1-b2cb-4062-a142-fb603e439adf)

- **Residuals Across Domain:**
  
  ![Residuals](https://github.com/user-attachments/assets/1e7ee7a8-69a2-4aef-939d-8626ad0f1afc)

- **Training Loss Curve:**
  
  ![TrainingLoss](https://github.com/user-attachments/assets/d2cadc18-4713-4227-9cf4-5d494aa4a82a)

