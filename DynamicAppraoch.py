def fibonacci_dynamic(n):
    """Generate Fibonacci series up to n terms using dynamic programming."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    
    return fib_series

# Example usage
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci series up to {n} terms (dynamic programming):")
    print(fibonacci_dynamic(n))
