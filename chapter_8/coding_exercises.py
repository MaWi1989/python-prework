
def add_num(num_1, num_2):
    return num_1+num_2

add_num(4,5)

print("\n")
def is_prime(num):
    """Naive method of checking for primes."""
    for n in range(2,num):
        if num%n == 0:
            print("not prime")
            break
    else:
        print("prime")

is_prime(25)
