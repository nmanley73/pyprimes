# Noel Manley
# Computing the primes
P = []

# Loop through all the numbers to check for prime no's
for i in range(2, 100):
    # assume number is prime
    isprime = True
    # Loop through all values from 2 up to i
    for j in range(2, i):
        # see if j divides i
        if i % j == 0:
            # If it does, i isn't prime so exit the loop
            isprime = False
            break
    # If it i prime then append to P
    if isprime:
        P.append(i)
# Print out the list
print(P)
