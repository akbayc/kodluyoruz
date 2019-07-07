import numpy as np
from numpy.linalg import matrix_power

def bigfibonacci(n, mod):
    holder = []
    qm = np.array([
        [1, 1],
        [1, 0]
    ])
    
    while n != 1:
        if n%2:
            holder.append(qm)
                   
        n //= 2
        qm = matrix_power(qm,2) % mod
                        
    if holder:
        for m in holder:
            qm = np.matmul(qm, m)
    result = qm%mod

    return result[0,1]



