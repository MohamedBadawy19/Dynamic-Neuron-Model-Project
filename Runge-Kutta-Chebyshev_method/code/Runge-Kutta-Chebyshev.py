import numpy as np
import matplotlib.pyplot as plt

# Neuron model parameters
C = 100  # Capacitance (pF)
vr = -60  # Resting potential (mV)
vt = -40  # Threshold potential (mV)
k = 0.7  # Gain parameter
a = 0.03  # Recovery time scale
b = -2  # Sensitivity of recovery to subthreshold fluctuations
c = -50  # After-spike reset value for v (mV)
d = 20  # After-spike increment for w
vpeak = 35  # Spike cutoff value (mV)
I = 100  # Input current (pA)

# Initial conditions
v0 = vr
w0 = 0
T = 20  # Total simulation time (ms)
dt = 0.25  # Time step (ms)
steps = int(T / dt)


def neuron_ode(v, w, I):
    dv = (k * (v - vr) * (v - vt) - w + I) / C
    dw = a * (b * (v - vr) - w)
    return dv, dw


def rkc_solver():
    v = np.zeros(steps + 1)
    w = np.zeros(steps + 1)
    t = np.arange(0, T + dt, dt)
    v[0] = v0
    w[0] = w0
    iteration_data = []

    # RKC parameters
    s = 4  # Number of stages
    mu = 1.0  # Damping parameter
    tau = 1.0 / (mu ** 2)

    for i in range(steps):
        if v[i] >= vpeak:
            v[i] = vpeak
            v[i + 1] = c
            w[i + 1] = w[i] + d
            iteration_data.append({
                'step': i,
                'time': i * dt,
                'v_before': v[i],
                'w_before': w[i],
                'iterations': 0,
                'v_after': v[i + 1],
                'w_after': w[i + 1],
                'message': 'Spike detected - reset values'
            })
            continue

        # Store initial values
        current_v = v[i]
        current_w = w[i]

        # First stage
        dv, dw = neuron_ode(current_v, current_w, I)
        y0 = np.array([current_v, current_w])
        f0 = np.array([dv, dw])
        y1 = y0 + (dt / s) * f0

        # Chebyshev recurrence
        y_prev = y0
        y_curr = y1

        for j in range(2, s + 1):
            theta = np.pi / (2 * s)
            theta_j = (j - 1) * theta
            omega_0 = 1.0 + np.sin(theta) ** 2 / 3.0
            omega_j = 1.0 + np.sin(theta_j) ** 2 / 3.0

            if j == 2:
                beta = (2 * omega_j) / omega_0
            else:
                beta = (4 * omega_j) / omega_0

            alpha = beta / tau

            # Evaluate derivative at current stage
            fj = np.array(neuron_ode(y_curr[0], y_curr[1], I))

            # Update solution
            y_new = (1 - alpha) * y_prev + alpha * y_curr + beta * (dt / s) * fj

            y_prev = y_curr
            y_curr = y_new

        # Store results
        v[i + 1], w[i + 1] = y_curr

        iteration_data.append({
            'step': i,
            'time': i * dt,
            'v_before': current_v,
            'w_before': current_w,
            'iterations': s,
            'v_after': v[i + 1],
            'w_after': w[i + 1],
            'message': 'RKC update'
        })

        if v[i + 1] < -100:
            print(f"Warning: Abnormal voltage detected at t={i * dt} ms: {v[i + 1]} mV")

    return v, w, iteration_data


# Run the simulation
v_rkc, w_rkc, iteration_data = rkc_solver()

# Print iteration details
print("Iteration Details:")
print(
    f"{'Step':<6} {'Time':<8} {'Iterations':<10} {'v_before':<10} {'w_before':<10} {'v_after':<10} {'w_after':<10} {'Message':<20}")
for data in iteration_data[:50]:  # Print first 50 steps
    print(
        f"{data['step']:<6} {data['time']:<8.2f} {data['iterations']:<10} {data['v_before']:<10.4f} {data['w_before']:<10.4f} {data['v_after']:<10.4f} {data['w_after']:<10.4f} {data['message']:<20}")

# Create time vector
time = np.arange(0, T + dt, dt)

# Plotting
plt.figure(figsize=(14, 10))

# Plot membrane potential
plt.subplot(2, 2, 1)
plt.plot(time, v_rkc, 'b', label='Membrane Potential')
plt.axhline(y=vpeak, color='r', linestyle='--', label='Spike Threshold')
plt.title('RKC: Membrane Potential (v)')
plt.ylabel('Voltage (mV)')
plt.xlabel('Time (ms)')
plt.legend()
plt.grid(True)
plt.ylim(-80, 40)

# Plot recovery variable
plt.subplot(2, 2, 2)
plt.plot(time, w_rkc, 'g', label='Recovery Variable')
plt.title('Recovery Variable (w)')
plt.xlabel('Time (ms)')
plt.ylabel('Recovery')
plt.legend()
plt.grid(True)

# Phase plane plot
plt.subplot(2, 2, 3)
plt.plot(v_rkc, w_rkc, 'm')
plt.title('Phase Plane (w vs v) - RKC')
plt.xlabel('Voltage (v) [mV]')
plt.ylabel('Recovery (w)')
plt.grid(True)

# Zoomed phase plane
plt.subplot(2, 2, 4)
plt.plot(v_rkc, w_rkc, 'm')
plt.title('Zoomed Phase Plane')
plt.xlabel('Voltage (v) [mV]')
plt.ylabel('Recovery (w)')
plt.xlim(-70, 40)
plt.ylim(min(w_rkc) - 10, max(w_rkc) + 10)
plt.grid(True)

plt.tight_layout()
plt.show()

# Results summary
print("\nSummary of Results:")
print(f"Maximum voltage: {max(v_rkc):.2f} mV")
print(f"Minimum voltage: {min(v_rkc):.2f} mV")
print(f"Number of spikes: {len([i for i in range(len(v_rkc)) if v_rkc[i] == vpeak])}")