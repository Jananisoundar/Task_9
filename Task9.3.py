# using the python lambda function create a Fibonacci series from 1 to 50 elements?
# Function to generate Fibonacci series using iteration
def generate_fibonacci_series(n):
    fib_series = [0, 1]
    any(map(lambda _: fib_series.append(fib_series[-1] + fib_series[-2]), range(2, n)))
    return fib_series

# Generate the first 50 elements of the Fibonacci series
fib_series = generate_fibonacci_series(50)

print(fib_series)

