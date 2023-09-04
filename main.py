# Function to check if a number is even or odd
def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

# Function to find factors of a number
def get_factors(number):
    factors = []
    iteration_index = 1
    while iteration_index <= number:
        if number % iteration_index == 0:
            factors.append(iteration_index)
        iteration_index += 1
    print(f'The factors of {number} are: {factors}')
    return factors

# Function to check if a number is prime based on its factors
def check_prime(number, factors):
    if len(factors) == 2:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')

# Function to analyze a number's properties
def analyze_number(number):
    check_odd_even(number)     # Check if the number is even or odd
    factors = get_factors(number)  # Get the factors of the number
    check_prime(number, factors)  # Check if the number is prime based on its factors
# Analyze various numbers using the analyze_number function
analyze_number(4)   # Analyze the number 4
analyze_number(7)   # Analyze the number 7
analyze_number(12)  # Analyze the number 12
analyze_number(17)  # Analyze the number 17
analyze_number(29)  # Analyze the number 29
  