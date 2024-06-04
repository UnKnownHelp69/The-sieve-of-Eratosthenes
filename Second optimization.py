n = int(input())

primes = [i for i in range(1, n + 1, 2)]

primes[0] = 0

for i in range(1, n//2):
    if primes[i] != 0:
        for j in range(i+primes[i], (n+1)//2, primes[i]):
            primes[j] = 0

primes = [i for i in primes if i != 0]

print(primes)