import numpy as np
import matplotlib.pyplot as plt
import time

# Neuron model parameters
C = 100  # Capacitance (pF)
vr = -60  # Resting potential (mV)
vt = -40  # Threshold potential (mV)
k = 0.7  # Gain parameter
a = 0.03  # Recovery time scale
b = -2  # Sensitivity of recovery to subthreshold fluctuations
c = -50  # After-spike reset value for v (mV)
d = 100  # After-spike increment for w
vpeak = 35  # Spike cutoff value (mV)
I = 100  # Input current (pA)

# Initial conditions
v0 = vr
w0 = 0
T = 1000  # Total simulation time (ms)
dt = 0.25  # Time step (ms)
steps = int(T / dt)  # Number of steps

# Reference values for validation
reference_v = [-60.0000, -54.4819, -50.6154, -49.5530, -53.6973]
reference_w = [0.0000, 6.2834, 59.0910, -12.4763, 1.5649]
reference_times = [0, 250, 500, 750, 1000]


def neuron_ode(v, w, I):
    """Define the Izhikevich neuron model ODEs"""
    dv = (k * (v - vr) * (v - vt) - w + I) / C
    dw = a * (b * (v - vr) - w)
    return dv, dw


def backward_euler():
    """Implement the Backward Euler method with Newton iterations"""
    start_time = time.time()

    # Initialize arrays
    v = np.zeros(steps + 1)
    w = np.zeros(steps + 1)
    t = np.arange(0, T + dt, dt)
    v[0] = v0
    w[0] = w0
    iteration_data = []

    for i in range(steps):
        # Spike detection and reset
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

        current_v = v[i]
        current_w = w[i]

        # Initial guess using forward Euler
        dv, dw = neuron_ode(current_v, current_w, I)
        next_v = current_v + dt * dv
        next_w = current_w + dt * dw

        # Newton iteration parameters
        tolerance = 1e-6
        max_iter = 100
        iteration_count = 0

        # Newton iteration loop
        for _ in range(max_iter):
            iteration_count += 1

            # Evaluate functions
            f_v, f_w = neuron_ode(next_v, next_w, I)
            F1 = next_v - current_v - dt * f_v
            F2 = next_w - current_w - dt * f_w

            # Jacobian matrix elements
            J11 = 1 - dt * (k * (2 * next_v - vr - vt) / C)
            J12 = -dt * (-1 / C)
            J21 = -dt * (a * b)
            J22 = 1 - dt * (-a)

            # Solve linear system
            det = J11 * J22 - J12 * J21
            if det == 0:
                break

            delta_v = (F2 * J12 - F1 * J22) / det
            delta_w = (F1 * J21 - F2 * J11) / det

            # Update solution
            next_v += delta_v
            next_w += delta_w

            # Check convergence
            if abs(delta_v) < tolerance and abs(delta_w) < tolerance:
                break

        # Store results
        v[i + 1] = next_v
        w[i + 1] = next_w

        iteration_data.append({
            'step': i,
            'time': i * dt,
            'v_before': current_v,
            'w_before': current_w,
            'iterations': iteration_count,
            'v_after': next_v,
            'w_after': next_w,
            'message': 'Normal update'
        })

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nExecution Time: {execution_time:.4f} seconds")

    return v, w, iteration_data


def find_time_index(times, target_time, dt):
    """Find array index corresponding to a specific time"""
    return int(target_time / dt)


def calculate_errors(v, w, reference_v, reference_w, reference_times, dt):
    """Calculate errors at reference time points"""
    errors = []
    for i, t in enumerate(reference_times):
        idx = find_time_index(np.arange(0, len(v) * dt, dt), t, dt)
        if idx < len(v):
            error_v = abs(v[idx] - reference_v[i])
            error_w = abs(w[idx] - reference_w[i])
            errors.append({
                'time': t,
                'v': v[idx],
                'w': w[idx],
                'reference_v': reference_v[i],
                'reference_w': reference_w[i],
                'error_v': error_v,
                'error_w': error_w
            })
        else:
            errors.append({
                'time': t,
                'v': None,
                'w': None,
                'reference_v': reference_v[i],
                'reference_w': reference_w[i],
                'error_v': None,
                'error_w': None,
                'message': 'Time exceeds simulation duration'
            })
    return errors


# Main simulation function
def main():
    # Run the simulation
    v_be, w_be, iteration_data = backward_euler()

    # Print iteration details for first 50 steps
    print("\nIteration Details (first 50 steps):")
    print(
        f"{'Step':<6} {'Time':<8} {'Iterations':<10} {'v_before':<10} {'w_before':<10} {'v_after':<10} {'w_after':<10} {'Message':<20}")
    for data in iteration_data[:50]:
        print(
            f"{data['step']:<6} {data['time']:<8.2f} {data['iterations']:<10} {data['v_before']:<10.4f} {data['w_before']:<10.4f} {data['v_after']:<10.4f} {data['w_after']:<10.4f} {data['message']:<20}")

    # Calculate and print errors
    errors = calculate_errors(v_be, w_be, reference_v, reference_w, reference_times, dt)
    print("\nError Analysis at Reference Times:")
    print(
        f"{'Time (ms)':<10} {'v(t)':<15} {'Reference v':<15} {'Error v':<15} {'w(t)':<15} {'Reference w':<15} {'Error w':<15}")
    for error in errors:
        if 'message' in error:
            print(f"{error['time']:<10} {error['message']}")
        else:
            print(
                f"{error['time']:<10} {error['v']:<15.4f} {error['reference_v']:<15.4f} {error['error_v']:<15.4f} {error['w']:<15.4f} {error['reference_w']:<15.4f} {error['error_w']:<15.4f}")

    # Create time vector
    time = np.arange(0, T + dt, dt)

<<<<<<< HEAD
    # Plotting
    plt.figure(figsize=(14, 10))

    # Plot membrane potential
    plt.subplot(2, 2, 1)
    plt.plot(time, v_be, 'b', label='Membrane Potential')
    plt.axhline(y=vpeak, color='r', linestyle='--', label='Spike Threshold')
    plt.title('Backward Euler: Membrane Potential (v)')
    plt.ylabel('Voltage (mV)')
    plt.xlabel('Time (ms)')
    plt.legend()
    plt.grid(True)
    plt.ylim(-80, 40)
=======
# Plot membrane potential
plt.subplot(2, 2, 1)
plt.plot(time, v_be, 'b', label='Membrane Potential')
plt.axhline(y=vpeak, color='r', linestyle='--', label='Spike Threshold')
plt.title('Backward Euler: Membrane Potential (v)')
plt.ylabel('Membrane Potential (mV)')
plt.xlabel('Time (ms)')
plt.legend()
plt.grid(True)
plt.ylim(-80, 40)  # Adjust scale to cover -70 to +40

# Plot recovery variable
plt.subplot(2, 2, 2)
plt.plot(time, w_be, 'g', label='Recovery Variable')
plt.title('Recovery Variable (pA)')
plt.xlabel('Time (ms)')
plt.ylabel('Recovery Variable (w)')
plt.legend()
plt.grid(True)
>>>>>>> 967e097bd15b6b829bbd946a76019fb69ef1b65a

    # Plot recovery variable
    plt.subplot(2, 2, 2)
    plt.plot(time, w_be, 'g', label='Recovery Variable')
    plt.title('Recovery Variable (w)')
    plt.xlabel('Time (ms)')
    plt.ylabel('Recovery')
    plt.legend()
    plt.grid(True)

    # Phase plane plot
    plt.subplot(2, 2, 3)
    plt.plot(v_be, w_be, 'm')
    plt.title('Phase Plane (w vs v) - Backward Euler')
    plt.xlabel('Voltage (v) [mV]')
    plt.ylabel('Recovery (w)')
    plt.grid(True)

    # Zoomed phase plane
    plt.subplot(2, 2, 4)
    plt.plot(v_be, w_be, 'm')
    plt.title('Zoomed Phase Plane')
    plt.xlabel('Voltage (v) [mV]')
    plt.ylabel('Recovery (w)')
    plt.xlim(-70, 40)
    plt.ylim(min(w_be) - 10, max(w_be) + 10)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # Results summary
    print("\nResults Summary:")
    print(f"Maximum voltage: {max(v_be):.2f} mV")
    print(f"Minimum voltage: {min(v_be):.2f} mV")
    print(f"Number of spikes: {len([i for i in range(len(v_be)) if v_be[i] == vpeak])}")


if __name__ == "__main__":
    main()