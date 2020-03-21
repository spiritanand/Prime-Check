import math
num = int(input("Enter the number to be checked :- "))


def is_prime2(num):

    """
    Better method of checking for primes.
    """
    if num == 1:
        return "None"
    elif num == 3 or num == 2:
        print(True)
    elif num % 2 == 0:
        print(False)
    else:
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                print(False)
                exit()
        print(True)


is_prime2(num)
