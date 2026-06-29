"""
Fibonacci Sequence Generator using Recursion with Memoization
"""

def fibonacci_recursive(n, memo=None):
    """
    Calculate the nth Fibonacci number using recursive approach with memoization.
    
    Args:
        n (int): The position in the Fibonacci sequence
        memo (dict): Dictionary to store previously calculated values
        
    Returns:
        int: The nth Fibonacci number
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
    return memo[n]


def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using iterative approach.
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def fibonacci_sequence(n):
    """
    Generate the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): How many Fibonacci numbers to generate
        
    Returns:
        list: List of the first n Fibonacci numbers
    """
    sequence = []
    for i in range(n):
        sequence.append(fibonacci_iterative(i))
    return sequence


if __name__ == "__main__":
    # Example usage
    print("Fibonacci Sequence Generator")
    print("=" * 40)
    
    # Generate first 10 Fibonacci numbers
    n = 10
    print(f"\nFirst {n} Fibonacci numbers:")
    print(fibonacci_sequence(n))
    
    # Get specific Fibonacci numbers
    print(f"\nFibonacci(15) using recursion: {fibonacci_recursive(15)}")
    print(f"Fibonacci(15) using iteration: {fibonacci_iterative(15)}")
    
    # Generate and display larger sequence
    n = 15
    print(f"\nFirst {n} Fibonacci numbers:")
    fib_seq = fibonacci_sequence(n)
    for i, fib in enumerate(fib_seq):
        print(f"F({i}) = {fib}")
