import numpy as np
import matplotlib.pyplot as plt
import time
#-------------------------
## Para
C=100
vr = -60 
vt = -40
k = 0.7
an = 0.03
bn = -2
cn =-50
dn =100
vpeak = 35
ncall = 0
nout = 1000
h= 1
#----------------
In = np.zeros(nout+2)
In[101:] = 70
v = np.zeros(nout+2)
w = np.zeros(nout+2)
v[0]=vr
w[0]=0
t = np.arange(0,nout+2,h)
###--------------------
def neuron(t,y):
    global ncall
    v = y[0]
    w = y[1]
    dvbydt = (k*(v - vr) * (v - vt) - w + In[i]) / C
    dwbydt = an * (bn * (v - vr) - w)
    ncall += 1
    return np.array([dvbydt, dwbydt])


def euler(h,t,y):
    deriv = neuron(t,y)
    y = y + (deriv*h)
    return y
#----------
def get_time():
    return time.time() * 1000
###------------------
start_time = get_time()
for i in range(0,nout+1):
    y = np.array([v[i],w[i]])
    yout=euler(h,t[i],y)
    v[i+1]=yout[0]
    w[i+1]=yout[1]
    if(v[i+1]>=vpeak):
        v[i]=vpeak
        v[i+1]=cn
        w[i+1]=w[i+1]+dn
###---------------------
end_time = get_time()

elapsed_time = end_time - start_time

print(f"elapsed time is : {elapsed_time}")


# Plotting v(t)
plt.figure(figsize=(10, 6))
plt.plot(t, v, 'b-', label='Membrane Potential v(t)')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('Dynamic Neuron Model: Membrane Potential vs. Time')
plt.grid(True)
plt.legend()
plt.show()

# Plotting w(t)
plt.figure(figsize=(10, 6))
plt.plot(t, w, 'r-', label='Recovery Variable w(t)')
plt.xlabel('Time (ms)')
plt.ylabel('Recovery Variable (pA)')
plt.title('Dynamic Neuron Model: Recovery Variable vs. Time')
plt.grid(True)
plt.legend()
plt.show()


# Plotting w vs. v (Phase Plane)
plt.figure(figsize=(8, 6))
plt.plot(v, w, 'g-', label='Phase Plane (w vs. v)')
plt.xlabel('Membrane Potential v (mV)')
plt.ylabel('Recovery Variable w (pA)')
plt.title('Dynamic Neuron Model: Phase Plane')
plt.grid(True)
plt.legend()
plt.show()
print(ncall)
print(f"\nComparison with Table 4.3a:")
print(f"t=0.0:   v[0] = {v[0]:.4f}, w[0] = {w[0]:.4f}")
print(f"t=250.0: v[250] = {v[251]:.4f}, w[250] = {w[251]:.4f}")
print(f"t=500.0: v[500] = {v[501]:.4f}, w[500] = {w[501]:.4f}")
print(f"t=750.0: v[750] = {v[751]:.4f}, w[750] = {w[751]:.4f}")
print(f"t=1000.0: v[1000] = {v[1001]:.4f}, w[1000] = {w[1001]:.4f}")