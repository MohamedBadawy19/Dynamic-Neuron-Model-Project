🧠 Brief Summary of the SEIL-PINN Code and Its Purpose
🎯 Goal
To solve the SEIL tuberculosis model using both:

a numerical method (Radau via solve_ivp)

and a Physics-Informed Neural Network (PINN)

Then compare both solutions in terms of accuracy and behavior.

🔧 Code Structure and Explanation
1. Model Parameters and Initial Conditions
Defined according to Table 7.2 of the textbook:

python
Copy
Edit
B, beta, mu, k, r1, r2, phi, gamma, d1, d2 = ...
S0 = B / mu, E0 = 0, I0 = 1, L0 = 0
These values define the ODE system and its biological meaning:

S: Susceptible

E: Exposed (not yet infectious)

I: Infectious

L: Loss-of-sight (untreated, possibly hidden)

2. Numerical Solver (solve_ivp)
This is a traditional ODE solver (Radau method) that solves the SEIL model equations.

python
Copy
Edit
sol_ref = solve_ivp(tb_ode, [0, 20], y0, ...)
Used to:

Generate reference solution ("ground truth")

Evaluate the error of the PINN later

Provide some training data points to guide the PINN

3. PINN Architecture (ImprovedPINN)
A fully-connected neural network trained to learn the solution 
𝑆
(
𝑡
)
,
𝐸
(
𝑡
)
,
𝐼
(
𝑡
)
,
𝐿
(
𝑡
)
S(t),E(t),I(t),L(t) from scratch.

Key features:

Time 
𝑡
t is the input, normalized to [−1, 1]

Output: 4 values (S, E, I, L), scaled to expected ranges

Uses softplus() to ensure outputs stay positive

Why improvements?

L is much smaller than other variables, so:

Smaller scaling factor

Gentler softplus activation

Larger weight in the loss function

This improves numerical stability and precision for L

4. Loss Function (compute_loss)
Three parts:

📘 A. Physics Loss
The derivatives of the neural network outputs are matched to the ODE system using autograd.

This enforces that the neural network respects the ODEs.

🧾 B. Initial Condition Loss
Forces the PINN output at 
𝑡
=
0
t=0 to match the known initial values.

🔖 C. Data Loss
Compares the PINN prediction to a small number of reference data points from solve_ivp for better convergence.

Special care is given to the L compartment, which is:

Small in magnitude

Harder to learn

Given much more weight in the loss

5. Training Strategy
Two-phase training:

Adam optimizer (fast, robust) – 8000 epochs

LBFGS optimizer (fine-tuning) – 100 steps

This improves:

Stability

Accuracy

Faster convergence

6. Evaluation and Plotting
Full solution plotted for S, E, I, L

Relative and absolute error calculations

Detailed printout of final populations and errors

Additional analysis for L:

Peak values

Time of maximum L

Relative error when L is significant

✅ Why This Approach Works
Combines the precision of numerical solvers with the flexibility of neural networks

Enforces physical constraints using the ODEs

Uses a learning-based model that can generalize beyond fixed solvers

Matches the project goals by comparing traditional vs. ML-based approaches
