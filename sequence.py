# Question 2: Fibonacci Sequence
def generate_fibonacci(limit):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
limit = 100
fibonacci_sequence = generate_fibonacci(limit)
print("Fibonacci sequence up to", limit, ":", fibonacci_sequence)
