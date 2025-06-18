import numpy as np
import matplotlib.pyplot as plt
"""
Here we intialize the parameters
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
In[101:]=70
v= np.zeros(1001)
w = np.zeros(1001)
##Initial Conditions
v[0] = vr
w[0] = 0
 
def f(i, y):
    """
    this method is used to calculate the derivative of dependent variable
    """
    v = y[0]
    w = y[1]
    dvbydt = (k*(v - vr) * (v - vt) - w + In[i]) / C
    dwbydt = a * (b * (v - vr) - w)
    return np.array([dvbydt, dwbydt])


### Heun's Method Implementation
for i in range(0, 1000):
    y = np.array([v[i],w[i]])
    derivatives = np.zeros(2)
    derivatives = f(i,y)
    y_predicted = y + h*derivatives
    y_corrected = y + (h/2)*(f(i,y)+f(i+1,y_predicted))
    v[i+1] = y_corrected[0]
    print(v[i+1])
    w[i+1] = y_corrected[1]
    if (v[i + 1] >= vpeak):
        v[i] = vpeak
        v[i + 1] = c
        w[i + 1] = w[i + 1] + d
    
def print_table(title, indices, v_values, w_values):
    print(f"\n{title}")
    print(f"{'Index':>6} | {'v (mV)':>10} | {'w (pA)':>10}")
    print("-" * 32)
    for i, v_val, w_val in zip(indices, v_values, w_values):
        print(f"{i:6} | {v_val:10.2f} | {w_val:10.2f}")

# Print values from index 96 to 105
start, end = 96, 106  # end is exclusive
print_table(f"Values of v and w from index {start} to {end - 1}", range(start, end), v[start:end], w[start:end])




t = np.arange(0, 1001, h)
plt.figure(figsize=(14, 10))
plt.subplot(2, 2, 1)
plt.plot(t, v, 'b-', label='Membrane Potential v(t)')
plt.axhline(y=vpeak, color='r', linestyle='--', label='Spike Threshold')
plt.title('Heuns Method : Membrane Potential (v)')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('Dynamic Neuron Model: Membrane Potential vs. Time')
plt.legend()
plt.grid(True)
plt.ylim(-80, 40)  # Adjust scale to cover -70 to +40

# Plotting w(t)
plt.subplot(2, 2, 2)
plt.plot(t, w, 'r-', label='Recovery Variable w(t)')
plt.xlabel('Time (ms)')
plt.ylabel('Recovery Variable (pA)')
plt.title('Recovery Variable (w)')
plt.legend()
plt.grid(True)


# Plotting w vs. v (Phase Plane)
plt.subplot(2, 2, 3)
plt.plot(v, w, 'g-', label='Phase Plane (w vs. v)')
plt.xlabel('Membrane Potential v (mV)')
plt.ylabel('Recovery Variable w (pA)')
plt.title('Phase Plane (w vs v) - Heun method ')
plt.legend()
plt.grid(True)

# Zoomed phase plane around the area of interest
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
print(f"Number of spikes: {len([i for i in range(len(v)) if v[i] == vpeak])}")
