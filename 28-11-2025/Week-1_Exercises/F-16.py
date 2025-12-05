
def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def primes_between(start, end):
    if start > end:
        start, end = end, start
    return [n for n in range(start, end + 1) if is_prime(n)]

print(primes_between(10, 40))
