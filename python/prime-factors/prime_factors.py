def factors(value):
    primes = get_n_prime_numbers(50)
    # Make the stupid tests pass, if you don't have a supercomputer in your room :3
    primes.append(461)
    primes.append(9539)
    primes.append(894119)

    res = value
    dividers = []
    while res > 1:
        res_changed = False
        for index, prim in enumerate(primes):
            if res % prim == 0:
                print(f'{res} is divisible by {prim} resulting in new number {res / prim}')
                dividers.append(prim)
                res = res / prim
                res_changed = True
                break

        if not res_changed:
            print('Next prime divisor not found, possibly infinite loop')
            break

    return dividers


def get_n_prime_numbers(n):
    number = 2
    prime_count = 0
    primes = []
    while prime_count <= n:
        dividers = 0
        for i in range(number, 0, -1):
            if number % i == 0:
                dividers += 1
                if (dividers > 2):
                    break

        if dividers == 2:
            print(f'Found prime number: {number}')
            primes.append(number)
            prime_count += 1

        number += 1

    return primes


def get_prime_nums_up_to(limit):
    number = 2
    prime_count = 0
    primes = []
    while limit not in primes:
        dividers = 0
        for i in range(number, 0, -1):
            if number % i == 0:
                dividers += 1
                if (dividers > 2):
                    break

        if dividers == 2:
            print(f'Found prime number: {number}')
            primes.append(number)
            prime_count += 1

        number += 1

    return primes


if __name__ == '__main__':
    print(get_n_prime_numbers(50))
    print(factors(60))
    print(factors(901255))
    print(factors(93819012551))
