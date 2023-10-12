
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def print_primes(num):
    for i in range(2, num+1):
        if is_prime(i):
            print(str(i) + " ")


if __name__ == '__main__':
    print_primes(19)
