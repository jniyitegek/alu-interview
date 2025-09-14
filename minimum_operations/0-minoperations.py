#!/usr/bin/python3
def minOperations(n):
    """
    Calculate the minimum number of operations needed to obtain exactly 'n' characters
    in a text file using only two operations: Copy All and Paste.

    Problem context:
        - You start with a single character 'H'.
        - You can:
            1. Copy All (copy all existing characters).
            2. Paste (paste the copied content).
        - The goal is to reach exactly 'n' characters with the fewest operations.

    Approach:
        - The minimum operations correspond to the sum of the prime factors of 'n'.
        - This is because you can "build up" the string in groups, multiplying
          characters by using Copy + Paste in chunks.
        - Example: n = 9 → factors: 3 * 3 → min operations = 3 + 3 = 6.

    Args:
        n (int): Target number of characters.

    Returns:
        int: Minimum number of operations required. Returns 0 if n < 2
             since you can’t build fewer than 2 characters.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2  # Start with the smallest prime number
    while n > 1:
        # While 'divisor' is a factor of n, keep dividing
        while n % divisor == 0:
            operations += divisor   # Each factor contributes to operations
            n //= divisor           # Reduce n by dividing out the factor
        divisor += 1                # Move to the next possible divisor
    return operations
