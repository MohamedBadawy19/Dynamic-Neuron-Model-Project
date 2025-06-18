import numpy as np
import matplotlib.pyplot as plt
import os

# --- Neuron Model Parameters ---
C = 100.0   # Capacitance (pF)
vr = -60.0  # Resting potential (mV)
vt = -40.0  # Threshold potential (mV)
k = 0.7     # Gain parameter
a = 0.03    # Recovery time scale
b = -2.0    # Sensitivity of recovery to subthreshold fluctuations
c = -50.0   # After-spike reset value for v (mV)
d = 100.0   # After-spike increment for w
vpeak = 35.0  # Spike cutoff value (mV)
I_stim = 700.0 # Input current (pA)

# --- Simulation Parameters ---
T = 200.0   # Total simulation time (ms)
dt_initial = 0.25 # Initial time step (ms)
t_stim_on = 10.0 # Time to turn stimulus on
t_stim_off = 190.0 # Time to turn stimulus off

# --- RKF45 Solver Parameters ---
TOL = 1e-5  # Error tolerance
H_MIN = 1e-4 # Minimum step size
H_MAX = 2.0  # Maximum step size
S = 0.98    # Safety factor for step size adjustment

def neuron_ode(t, v, w):
    """
    Defines the ODEs for the neuron model.
    Includes time-dependent input current I(t).
    """
    # Apply stimulus current only within the specified time window
    current = I_stim if t_stim_on <= t <= t_stim_off else 0.0
    
    dv_dt = (k * (v - vr) * (v - vt) - w + current) / C
    dw_dt = a * (b * (v - vr) - w)
    
    return np.array([dv_dt, dw_dt])

def rkf45_step(t, y, h, f):
    """
    Performs a single adaptive step of the Runge-Kutta-Fehlberg method.
    Args:
        t (float): Current time.
        y (np.array): Current state [v, w].
        h (float): Current step size.
        f (function): Function to compute derivatives f(t, v, w).
    Returns:
        (np.array, float): The 5th order solution (y_new) and the estimated error.
    """
    # Butcher Tableau coefficients for RKF45
    c_coeffs = [0., 1/4, 3/8, 12/13, 1., 1/2]
    a_coeffs = [
        [1/4],
        [3/32, 9/32],
        [1932/2197, -7200/2197, 7296/2197],
        [439/216, -8., 3680/513, -845/4104],
        [-8/27, 2., -3544/2565, 1859/4104, -11/40]
    ]
    
    # Coefficients for the 4th and 5th order solutions
    b4_coeffs = [25/216, 0., 1408/2565, 2197/4104, -1/5, 0.]
    b5_coeffs = [16/135, 0., 6656/12825, 28561/56430, -9/50, 2/55]
    
    # Calculate the six k-values
    k_vals = np.zeros((6, 2))
    k_vals[0] = f(t, y[0], y[1])
    for i in range(5):
        y_temp = y + h * sum(a_coeffs[i][j] * k_vals[j] for j in range(i + 1))
        k_vals[i+1] = f(t + c_coeffs[i+1] * h, y_temp[0], y_temp[1])
        
    # Calculate 4th and 5th order estimates
    y4 = y + h * sum(b * k for b, k in zip(b4_coeffs, k_vals))
    y5 = y + h * sum(b * k for b, k in zip(b5_coeffs, k_vals))
    
    # Estimate the error (difference between 5th and 4th order solutions)
    error = np.linalg.norm(y5 - y4)
    
    return y5, error

# --- Main Simulation Loop ---
# Initialize lists to store results
t_vals = [0.0]
v_vals = [vr]
w_vals = [vr]
h_vals = [dt_initial]

# Set initial state
t = 0.0
y = np.array([vr, vr]) # [v, w]
h = dt_initial
spike_count = 0

print("Starting adaptive RKF45 simulation...")
while t < T:
    # Check for spike condition from the *previous* step's result
    if y[0] >= vpeak:
        # Record the peak value for a clean plot
        v_vals.append(vpeak)
        w_vals.append(y[1])
        t_vals.append(t)
        h_vals.append(h)
        
        # Apply reset conditions
        y[0] = c
        y[1] = y[1] + d
        spike_count += 1
        
        # Store the post-reset state
        v_vals.append(y[0])
        w_vals.append(y[1])
        t_vals.append(t) # Same time point for the reset
        h_vals.append(h)

    # Prevent overshooting the end time
    if t + h > T:
        h = T - t
        
    # Perform an RKF45 step
    y_new, error = rkf45_step(t, y, h, neuron_ode)

    # --- Adaptive Step Size Control ---
    if error <= TOL or h <= H_MIN:
        # Step is accepted
        t += h
        y = y_new
        
        # Store results
        v_vals.append(y[0])
        w_vals.append(y[1])
        t_vals.append(t)
        h_vals.append(h)

    # Calculate optimal new step size, even if the step was accepted
    # Avoid division by zero if error is zero
    h_new = S * h * (TOL / error)**0.2 if error > 1e-15 else h * 2.0
    
    # Clamp the new step size to be within bounds
    h = np.clip(h_new, H_MIN, H_MAX)


print("Simulation finished.")
print(f"Total steps taken: {len(t_vals)}")
print(f"Number of spikes: {spike_count}")

# --- Plotting ---
output_dir = os.path.join("Dynamic-Neuron-Model-Project", "Runge-Kutta-Fehlburg", "plots")
os.makedirs(output_dir, exist_ok=True)

# Convert lists to numpy arrays for plotting
t_plot = np.array(t_vals)
v_plot = np.array(v_vals)
w_plot = np.array(w_vals)

# Create a combined figure for all plots
fig, axs = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Adaptive RKF45 Neuron Simulation Results', fontsize=16)

# Plot 1: Membrane Potential
axs[0, 0].plot(t_plot, v_plot, 'b-', label='v(t)')
axs[0, 0].axhline(y=vpeak, color='r', linestyle='--', label='Spike Threshold')
axs[0, 0].set_title('Membrane Potential (v)')
axs[0, 0].set_xlabel('Time (ms)')
axs[0, 0].set_ylabel('Membrane Potential (mV)')
axs[0, 0].legend()
axs[0, 0].grid(True)
axs[0, 0].set_ylim(-80, 50)

# Plot 2: Recovery Variable
axs[0, 1].plot(t_plot, w_plot, 'r-', label='w(t)')
axs[0, 1].set_title('Recovery Variable (w)')
axs[0, 1].set_xlabel('Time (ms)')
axs[0, 1].set_ylabel('Recovery Variable (pA)')
axs[0, 1].legend()
axs[0, 1].grid(True)

# Plot 3: Phase Plane
axs[1, 0].plot(v_plot, w_plot, 'g-')
axs[1, 0].set_title('Phase Plane (w vs v)')
axs[1, 0].set_xlabel('Membrane Potential v (mV)')
axs[1, 0].set_ylabel('Recovery Variable w (pA)')
axs[1, 0].grid(True)

# Plot 4: Step Size Adaptation
axs[1, 1].plot(t_plot, h_vals, 'm-', label='Step Size (h)')
axs[1, 1].set_title('Adaptive Step Size')
axs[1, 1].set_xlabel('Time (ms)')
axs[1, 1].set_ylabel('Step Size (ms)')
axs[1, 1].set_yscale('log') # Use a log scale to see variations clearly
axs[1, 1].legend()
axs[1, 1].grid(True)

# Save the combined figure
plt.tight_layout(rect=[0, 0, 1, 0.96])
output_path_combined = os.path.join(output_dir, "rkf45_combined_results.png")
plt.savefig(output_path_combined, dpi=300)
plt.show()

print(f"\nPlots saved to: {output_path_combined}")
