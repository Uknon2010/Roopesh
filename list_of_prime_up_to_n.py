from prime_numbers import is_prime


def list_prime_up_to_n(num):
    primes_up_to_n = []
    for i in range(2, num+1):
        if is_prime(i):
            primes_up_to_n.append(i)
    return primes_up_to_n

if __name__ == '__main__':
    n = 100
    primes = list_prime_up_to_n(n)
    print(f"primes_up_to {n} = {primes}")


