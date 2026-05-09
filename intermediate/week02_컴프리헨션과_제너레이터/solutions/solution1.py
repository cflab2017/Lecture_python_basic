def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))

primes = [n for n in range(2, 101) if is_prime(n)]
print(primes)
print(f"총 {len(primes)}개")
