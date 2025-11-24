# Finding prime numbers using python function
def is_prime(n):

    i = 1
    factors = 0
    while i <= n:
        if n % i == 0:
            factors = factors + 1
        i = i + 1
    if (factors == 2):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

is_prime(int(input("Please enter any number:")))

def check_number(n):
    i = 2
    is_prime = True
    while i < n:
        if n % i == 0:
            is_prime = False
            break
        i = i + 1
    return is_prime

is_prime = check_number(int(input("Please enter any number:")))
if (is_prime):
    print("Number is prime")
else:
    print("Number is not prime")
