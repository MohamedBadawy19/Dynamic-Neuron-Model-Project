# 🧠 Dynamic Neuron Model Project

This repository provides multiple numerical and deep learning approaches for solving the **Izhikevich neuron model** — a well-known system of two ordinary differential equations (ODEs) that simulate spiking neuron behavior efficiently.

## 📚 About the Izhikevich Model

The Izhikevich model is a biologically plausible spiking neuron model defined by the following two ODEs:

dv/dt = 0.04v² + 5v + 140 - u + I
du/dt = a(bv - u)

Where:
- `v` is the membrane potential of the neuron
- `u` is a membrane recovery variable
- `a`, `b`, `c`, and `d` are model parameters
- `I` is the synaptic input current

This model combines the biological plausibility of Hodgkin-Huxley-type models with the computational efficiency of integrate-and-fire models.

## 📁 Repository Contents

| File / Folder                        | Description |
|-------------------------------------|-------------|
| `Explicit_Euler_method/`            | Solves the Izhikevich model using the Explicit Euler method. |
| `Backward_Euler_method.py`          | A more stable integration using the Backward Euler method. |
| `Midpoint_(RK2)_method/`            | Implements the Midpoint (RK2) method. |
| `adaptive_exponential_Rosenbrock/`  | Advanced stiff solver using exponential Rosenbrock method. |
| `DL_PINN_model/`                    | Uses Physics-Informed Neural Networks (PINNs) to approximate the dynamics of the Izhikevich model. |
| `unity/`                            | (Optional) Unity files for visualization or interaction. |

## 🎯 Goals

- Explore different numerical integration methods for simulating Izhikevich neurons
- Compare solver stability, accuracy, and performance
- Introduce deep learning (PINNs) as an alternative solver
- Offer a clear structure for neuroscience or computational modeling projects

## 🚀 Getting Started

### Requirements

- Python 3.8+
- Required packages: `numpy`, `matplotlib`, `torch`, `scipy`
- Jupyter Notebook (optional)
- Unity (optional, for interactive visuals)

### Example Run

# Clone the repo
git clone https://github.com/MohamedBadawy19/Dynamic-Neuron-Model-Project.git
cd Dynamic-Neuron-Model-Project

# Run a method (example: Explicit Euler)
cd Explicit_Euler_method
python simulate_explicit_euler.py

Run the PINN (Physics-Informed Neural Network)

cd DL_PINN_model
python train_pinn.py

📊 Output

Each method generates output graphs such as:

Membrane potential v over time

Recovery variable u over time

Raster plots of spiking neuron activity (optional)


These help analyze the model's behavior and compare between solvers.

👨‍💻 Contributors

This is a collaborative educational project developed by Mohamed Badawy and contributors. See the GitHub contributors section for full credit.

📄 License

This project is licensed under the MIT License. You are free to use, modify, and share it with proper attribution.
