import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def midpoint_method(v_old , w_old , h_value , num_iter):
    # defining the arrays for dataframe rendering
    v_old_values = []
    v_new_values = []
    w_old_values = []
    w_new_values = []
    k_1_v_values = []
    k_1_w_values = []
    k_2_v_values = []
    k_2_w_values = []
    iterations   = []
    # defining the parameters that will be used in equations
    c = 100
    k = .7
    v_r = -60
    v_t = -40
    a = .03
    b = -2
    d = 100
    I_N = 0
    # looping "num_iter" number of iterations
    for i in range(num_iter):
        # if the iteration was larger than or equal to 101 , I_N will equal to 70
        if i + 1 >= 101:
            I_N = 70
        # calculating the K1v and K1w (Step 1)
        print(f"\nIter : {i + 1}")
        k_1_v = (1/c)*(k*(v_old - v_r)*(v_old - v_t) - w_old + I_N)
        k_1_w = a*(b*(v_old - v_r) - w_old)
        # calculating the mid value of v using k_1_v and mid value of w using k_1_w (Step 2)
        v_mid = v_old + (h_value / 2) * k_1_v
        w_mid = w_old + (h_value / 2) * k_1_w
        # calculating the K2v and K2w using mid values from Step 2 (Step 3)
        k_2_v = (1 / c) * (k * (v_mid - v_r) * (v_mid - v_t) - w_mid + I_N)
        k_2_w = a * (b * (v_mid - v_r) - w_mid)
        # calculating the new values of v and w using values from step 3 (Step 4)
        v_new = v_old + h_value * k_2_v
        w_new = w_old + h_value * k_2_w
        # appending the values to the arrays which intially declared for rendering the values using dataframe
        k_1_v_values.append(k_1_v)
        k_2_v_values.append(k_2_v)
        k_1_w_values.append(k_1_w)
        k_2_w_values.append(k_2_w)
        v_old_values.append(v_old)
        w_old_values.append(w_old)
        v_new_values.append(v_new)
        w_new_values.append(w_new)
        iterations.append(i)
        # checking the spike value if V became bigger than the spike value , then V of next iteration = -50 and W of next iteration = previous value of W + d
        if v_new >= 35: 
            v_old = -50
            w_old = w_new + d
        else:
            v_old = v_new
            w_old = w_new
    # rendering all the values calculated using dataframe from pandas
    df = pd.DataFrame({"v old" : v_old_values , "w old" : w_old_values , "K1v" : k_1_v_values , "k1w" : k_1_w_values , "K2v" : k_2_v_values , "K2w" : k_2_w_values , "v new" : v_new_values , "w new" : w_new_values} , index = iterations)
    # plotting the value of V (y-axis) , time (x-axis) in ms
    ax_1 = plt.subplot(2 , 2 , 1)
    ax_1.plot(iterations , v_old_values )
    ax_1.set_xlabel("Time in ms")
    ax_1.set_ylabel("V in midpoint method (RK2)")
    # plotting the value of W (y-axis) , time (x-axis) in ms
    ax_2 = plt.subplot(2 , 2 , 2)
    ax_2.plot(iterations , w_old_values)
    ax_2.set_xlabel("Time in ms")
    ax_2.set_ylabel("W in midpoint method (RK2)")
    # plotting the value of W (y-axis) , V (x-axis)
    ax_3 = plt.subplot(2 , 2 , (3 , 4))
    ax_3.plot(v_old_values , w_old_values)
    ax_3.set_xlabel("V in midpoint method (RK2)")
    ax_3.set_ylabel("W in midpoint method (RK2)")
    plt.show()
    df.to_csv("results.csv")
    print(df)
# initial values of Vo = -60 , Wo = 0 , time = 1 ms , number of iteraions = 1000
midpoint_method(-60 , 0 , 1 , 400)
    