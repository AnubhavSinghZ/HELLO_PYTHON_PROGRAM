# Define the infinite generator function
def count_to_infinity(n):
    while True:
        yield n
        n += 1  # Increment the counter safely

# Create the generator object starting at 10
counter = count_to_infinity(10)

# Call it whenever you need the next number
print(next(counter))  # Output: 10
print(next(counter))  # Output: 11
