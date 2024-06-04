n = int(input())

primes = [i for i in range(n + 1)]

primes[1] = 0

i = 2
while i*i <= n:
    if primes[i] != 0:
        j = i + i
        for j in range(i+i, n+1, i):
            primes[j] = 0
    i+=1

primes = [i for i in primes if i != 0]

print(primes)
