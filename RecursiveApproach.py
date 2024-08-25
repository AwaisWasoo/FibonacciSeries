def fibonacci_recursive(n):
    """Return the nth Fibonacci number using a recursive approach."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def generate_fibonacci_series(n):
    """Generate Fibonacci series up to n terms using the recursive approach."""
    return [fibonacci_recursive(i) for i in range(n)]

# Example usage
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci series up to {n} terms (recursive):")
    print(generate_fibonacci_series(n))
