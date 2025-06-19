import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
import pandas as pd
import time

start_time = time.time()
# Constants
C = 100
k = 0.7
vr = -60
vt = -40
a = 0.03
b = -2
v_peak = 35
c = -50
d = 100

# Simulation setup
T = 1000  # total time (ms)
h = 0.25  # initial step size
tol = 0.5  # tolerance for adaptive step
fac_min, fac_max = 0.1, 5
h_min, h_max = 0.01, 2.0

# Initial conditions
t_vals = [0]
v_vals = [vr]
w_vals = [0]
h_vals = [h]

# Table data
recorded_data = []

t = 0
v = vr
w = 0

while t < T:
    In = 0 if t < 101 else 70

    # Current state
    y = np.array([v, w])

    # Compute f(y)
    dvdt = (1 / C) * (k * (v - vr) * (v - vt) - w + In)
    dwdt = a * (b * (v - vr) - w)
    f = np.array([dvdt, dwdt])

    # Compute Jacobian
    dv_dv = (1 / C) * k * ((v - vr) + (v - vt))
    dv_dw = -1 / C
    dw_dv = a * b
    dw_dw = -a
    J = np.array([
        [dv_dv, dv_dw],
        [dw_dv, dw_dw]
    ])

    # First-order ExpRESS-Euler step
    I = np.eye(2)
    phi1 = inv(I - h * J)
    y1 = y + h * phi1 @ f

    # Half step + half step for error estimate (2nd-order Richardson)
    h_half = h / 2
    phi_half = inv(I - h_half * J)
    y_half = y + h_half * phi_half @ f

    v_half, w_half = y_half
    dvdt_half = (1 / C) * (k * (v_half - vr) * (v_half - vt) - w_half + In)
    dwdt_half = a * (b * (v_half - vr) - w_half)
    f_half = np.array([dvdt_half, dwdt_half])
    y2 = y_half + h_half * phi_half @ f_half

    # Error estimate
    err = np.linalg.norm(y1 - y2)
    err = max(err, 1e-10)  # Avoid divide-by-zero

    # Adaptive time step control
    if err < tol:
        t += h
        v, w = y2  # accept higher-order result
        if v >= v_peak:
            v = c
            w += d

        t_vals.append(t)
        v_vals.append(v)
        w_vals.append(w)
        h_vals.append(h)
        recorded_data.append([t, v, w, h])

        # Adjust h for next step
        h = h * min(max((tol / err) ** 0.5, fac_min), fac_max)
        h = min(max(h, h_min), h_max)
    else:
        # Reduce h and retry
        h = h * max((tol / err) ** 0.5, fac_min)
        h = max(h, h_min)

end_time = time.time()
# Print execution time
print(f"Execution time: {end_time - start_time:.8f} seconds")

# Plot v(t)
plt.figure(figsize=(10, 4))
plt.plot(t_vals, v_vals, color='tab:red')
plt.xlabel("Time (ms)")
plt.ylabel("v(t) [mV]")
plt.xlim(0, T)
plt.ylim(-60, 40)
plt.title("Adaptive ExpRESS-Euler: Membrane Potential v(t)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot w(t)
plt.figure(figsize=(10, 4))
plt.plot(t_vals, w_vals, color='tab:blue')
plt.xlabel("Time (ms)")
plt.ylabel("w(t) [mV]")
plt.xlim(0, T)
plt.ylim(-40, 70)
plt.title("Adaptive ExpRESS-Euler: Recovery Variable w(t)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot w(t) vs v(t)
plt.figure(figsize=(6, 6))
plt.plot(v_vals, w_vals, color='tab:green')
plt.xlabel("v(t) [mV]")
plt.ylabel("w(t) [mV]")
plt.title("Phase Plane: w(t) vs v(t)")
plt.xlim(-60, 40)
plt.ylim(-40, 70)
plt.grid(True)
plt.tight_layout()
plt.show()

# Create a DataFrame of the table
import pandas as pd
results_df = pd.DataFrame(recorded_data, columns=['Time (ms)', 'v (mV)', 'w', 'Step size h'])
print(results_df.iloc[50:61])
