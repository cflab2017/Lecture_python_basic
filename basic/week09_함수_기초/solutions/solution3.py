def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

primes = [n for n in range(1, 51) if is_prime(n)]
print("1~50 사이의 소수:")
print(*primes)
