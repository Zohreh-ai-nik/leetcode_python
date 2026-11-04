# Find and return all the prime numbers in an array of integers. If there are no prime numbers, return an empty array.

def find_primes(lst):
    primes = []
    for num in lst:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

lst = [2, 4, 6, 7, 9, 13]
print(find_primes(lst))