import numpy as np
l = np.array([0, 2, 3, 4, 5,6])
p = np.array([0,45,230,100,120,150])
n = 6
print("Length of stock:",l)
print("Price of each stock:",p)

def ExtendedBottomUpCutStock(p_array, n_array):
    r = np.array([0, 0, 0, 0, 0, 0])    # optimal value for rods of length 0..n
    s = np.array([0, 0, 0, 0, 0, 0])   # optimal first cut for rods of length 0..n
    r[0] = 0
    for j in range(1, n):
        q = 0
        for i in range(1, j+1):  # Find the max cut position for length j
            if (q < p[i] + r[j-i]):
                q = p[i] + r[j-i]
                s[j] = i   # Remember the value of best so far value of i
                r[j] = q
    print("Optimal value for rods of length 0 to n: ", r) #Optimal value for rods of length 0 to n
    i = n-1
    while (i > 0):
        i = i - s[i]
    print("Optimal First cut for rods of length 0 to n: ",s) #Optimal First cut for rods of length 0 to n
    return 1
        
a = ExtendedBottomUpCutStock(p, n)