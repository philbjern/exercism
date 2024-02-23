def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")

    primes = []
    i = 2
    while len(primes) < number:
        div_count = 0
        for divs in range(1, i+1):
            if i % divs == 0:
                div_count += 1

        if div_count == 2:
            primes.append(i)
            print(f'found prime: {i}')

        div_count = 0
        i += 1

    return primes[number - 1]


if __name__ == "__main__":
    print(prime(6))
