from sympy import primerange, isprime

def calculate_prime_gaps_and_twin_primes(start, end):
    primes = list(primerange(start, end))
    prime_gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
    sum_of_prime_gaps = sum(prime_gaps)
    
    twin_primes = sum(1 for i in range(len(prime_gaps)) if prime_gaps[i] == 2)
    
    return sum_of_prime_gaps, twin_primes

def filter_prime_numbers(numbers):
    return [num for num in numbers if isprime(num)]

# Calculate prime gaps and twin primes
start1, end1 = 600000, 699999
start2, end2 = 700000, 799999

sum_of_prime_gaps1, twin_primes1 = calculate_prime_gaps_and_twin_primes(start1, end1)
sum_of_prime_gaps2, twin_primes2 = calculate_prime_gaps_and_twin_primes(start2, end2)

print(f"Sum of prime gaps in range {start1}-{end1}: {sum_of_prime_gaps1}")
print(f"Number of twin primes in range {start1}-{end1}: {twin_primes1}")
print(f"Sum of prime gaps in range {start2}-{end2}: {sum_of_prime_gaps2}")
print(f"Number of twin primes in range {start2}-{end2}: {twin_primes2}")

# Filter prime numbers from a list
numbers = [123456789, 987654321, 999983, 999979, 999961]
prime_numbers = filter_prime_numbers(numbers)

print(f"Prime numbers in the list: {prime_numbers}")
