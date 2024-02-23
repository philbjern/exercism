def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")

    primes = prime_sieve(104743)
    return primes[number - 1]


def prime_sieve(number):
    """Find n first primes using sieve of Eratosthenes"""
    sieve = [True] * (number + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(number ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, number + 1, i):
                sieve[j] = False

    return [i for i in range(2, number + 1) if sieve[i]]


if __name__ == "__main__":
    # print(prime(6))
    print(prime_sieve(6))
