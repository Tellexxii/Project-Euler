def eratosthenes(n):     
    sieve = list(range(n + 1))
    sieve[1] = 0    
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

import time
start_time = time.time()

unzeroed = [x for x in eratosthenes(10000000) if x != 0]

print(unzeroed[10001])