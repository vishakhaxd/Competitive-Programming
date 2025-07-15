import sys

def is_interesting(n):
    S = 0
    count_2 = 0
    count_3 = 0

    # Compute sum of digits and count of 2s and 3s
    for digit in n:
        d = int(digit)
        S += d
        if d == 2:
            count_2 += 1
        elif d == 3:
            count_3 += 1

    # DP table for remainders modulo 9
    dp = [False] * 9
    dp[S % 9] = True  # Base case: original sum modulo 9

    # Process `2`s (adding +2)
    for _ in range(count_2):
        new_dp = dp[:]  # Copy previous state
        for r in range(9):
            if dp[r]:
                new_dp[(r + 2) % 9] = True  # Transition by adding 2
        dp = new_dp  # Update DP table

    # Process `3`s (adding +6)
    for _ in range(count_3):
        new_dp = dp[:]  # Copy previous state
        for r in range(9):
            if dp[r]:
                new_dp[(r + 6) % 9] = True  # Transition by adding 6
        dp = new_dp  # Update DP table

    return "YES" if dp[0] else "NO"

# Fast input handling
input = sys.stdin.read
data = input().split()
t = int(data[0])
results = []

for i in range(1, t + 1):
    n = data[i]
    results.append(is_interesting(n))

# Output results efficiently
sys.stdout.write("\n".join(results) + "\n")
