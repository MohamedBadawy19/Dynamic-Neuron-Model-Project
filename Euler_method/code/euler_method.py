import numpy as np
import matplotlib.pyplot as plt
import os

"""
Here we initialize the parameters
"""
C = 100
k = 0.7
vr = -60
vt = -40
a = 0.03
b = -2
c = -50
d = 100
vpeak = 35
h = 1
In = np.zeros(1001)
In[101:] = 70
v = np.zeros(1001)
w = np.zeros(1001)
## Initial Conditions
v[0] = vr
w[0] = 0

def f(i, y):
    """
    This method is used to calculate the derivative of dependent variables
    """
    v = y[0]
    w = y[1]
    dvbydt = (k * (v - vr) * (v - vt) - w + In[i]) / C
    dwbydt = a * (b * (v - vr) - w)
    return np.array([dvbydt, dwbydt])

### Explicit Euler Method Implementation
def euler(v, w, In, h, f, vpeak, c, d):
    spikes = 0  # Counter for spikes
    for i in range(0, 1000):
        y = np.array([v[i], w[i]])
        derivatives = f(i, y)
        y_next = y + h * derivatives
        v[i+1] = y_next[0]
        w[i+1] = y_next[1]
        if v[i+1] >= vpeak:
            v[i] = vpeak
            v[i+1] = c
            w[i+1] = w[i+1] + d
            spikes += 1  # Increment spike counter
    return spikes

spikes = euler(v, w, In, h, f, vpeak, c, d)

def print_table(title, indices, v_values, w_values):
    print(f"\n{title}")
    print(f"{'Index':>6} | {'v (mV)':>10} | {'w (pA)':>10}")
    print("-" * 32)
    for i, v_val, w_val in zip(indices, v_values, w_values):
        print(f"{i:6} | {v_val:10.2f} | {w_val:10.2f}")

# Print values from index 96 to 105
start, end = 96, 106  # end is exclusive
print_table(f"Values of v and w from index {start} to {end - 1}", range(start, end), v[start:end], w[start:end])

# Create directory for saving plots if it doesn't exist
output_dir = "Dynamic-Neuron-Model-Project\Euler_method\plots"
os.makedirs(output_dir, exist_ok=True)

# Time array for plotting
t = np.arange(0, 1001, h)

# Plot 1: Membrane Potential
plt.figure(figsize=(7, 5))
plt.plot(t, v, 'b-', label='Membrane Potential v(t)')
plt.axhline(y=vpeak, color='r', linestyle='--', label='Spike Threshold')
plt.title('Explicit Euler Method: Membrane Potential (v)')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.legend()
plt.grid(True)
plt.ylim(-80, 40)
output_path_v = os.path.join(output_dir, "euler_v.png")
plt.savefig(output_path_v, dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Recovery Variable
plt.figure(figsize=(7, 5))
plt.plot(t, w, 'r-', label='Recovery Variable w(t)')
plt.xlabel('Time (ms)')
plt.ylabel('Recovery Variable (pA)')
plt.title('Recovery Variable (w)')
plt.legend()
plt.grid(True)
output_path_w = os.path.join(output_dir, "euler_w.png")
plt.savefig(output_path_w, dpi=300, bbox_inches='tight')
plt.close()

# Plot 3: Phase Plane
plt.figure(figsize=(7, 5))
plt.plot(v, w, 'g-', label='Phase Plane (w vs. v)')
plt.xlabel('Membrane Potential v (mV)')
plt.ylabel('Recovery Variable w (pA)')
plt.title('Phase Plane (w vs v) - Explicit Euler Method')
plt.legend()
plt.grid(True)
output_path_phase = os.path.join(output_dir, "euler_phase_plane.png")
plt.savefig(output_path_phase, dpi=300, bbox_inches='tight')
plt.close()

# Plot 4: Zoomed Phase Plane
plt.figure(figsize=(7, 5))
plt.plot(v, w, 'm')
plt.title('Zoomed Phase Plane')
plt.xlabel('Voltage (v) [mV]')
plt.ylabel('Recovery (w)')
plt.xlim(-70, 40)
plt.ylim(min(w) - 10, max(w) + 10)
plt.grid(True)
output_path_zoomed = os.path.join(output_dir, "euler_zoomed_phase_plane.png")
plt.savefig(output_path_zoomed, dpi=300, bbox_inches='tight')
plt.close()

# Display all plots
plt.figure(figsize=(14, 10))

# Membrane potential
plt.subplot(2, 2, 1)
plt.plot(t, v, 'b-', label='Membrane Potential v(t)')
plt.axhline(y=vpeak, color='r', linestyle='--', label='Spike Threshold')
plt.title('Explicit Euler Method: Membrane Potential (v)')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.legend()
plt.grid(True)
plt.ylim(-80, 40)

# Recovery variable
plt.subplot(2, 2, 2)
plt.plot(t, w, 'r-', label='Recovery Variable w(t)')
plt.xlabel('Time (ms)')
plt.ylabel('Recovery Variable (pA)')
plt.title('Recovery Variable (w)')
plt.legend()
plt.grid(True)

# Phase plane
plt.subplot(2, 2, 3)
plt.plot(v, w, 'g-', label='Phase Plane (w vs. v)')
plt.xlabel('Membrane Potential v (mV)')
plt.ylabel('Recovery Variable w (pA)')
plt.title('Phase Plane (w vs v) - Explicit Euler Method')
plt.legend()
plt.grid(True)

# Zoomed phase plane
plt.subplot(2, 2, 4)
plt.plot(v, w, 'm')
plt.title('Zoomed Phase Plane')
plt.xlabel('Voltage (v) [mV]')
plt.ylabel('Recovery (w)')
plt.xlim(-70, 40)
plt.ylim(min(w) - 10, max(w) + 10)
plt.grid(True)

plt.tight_layout()
plt.show()

print("\nSummary of Results:")
print(f"Maximum voltage: {max(v):.2f} mV")
print(f"Minimum voltage: {min(v):.2f} mV")
print(f"Number of spikes: {spikes}")
print(f"Plots saved to:")
print(f"- Membrane Potential: {output_path_v}")
print(f"- Recovery Variable: {output_path_w}")
print(f"- Phase Plane: {output_path_phase}")
print(f"- Zoomed Phase Plane: {output_path_zoomed}")