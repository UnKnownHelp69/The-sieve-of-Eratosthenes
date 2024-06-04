n = int(input())

primes = [i for i in range(n + 1)]

primes[1] = 0

for i in range(2, n+1):
    if primes[i] != 0:
        for j in range(i+i, n+1, i):
            primes[j] = 0

primes = [i for i in primes if i != 0]

print(primes)