def solve():
    a = input().strip()
    b = input().strip()
    c = input().strip()

    n, m = len(a), len(b)
    # dp[i][j] = minimum number of changes needed to match the first (i+j) characters of c
    # by using the first i characters of a and the first j characters of b.
    dp = [[10 ** 9] * (m + 1) for _ in range(n + 1)]

    # Base case: matching an empty prefix of a and b with the empty prefix of c
    dp[0][0] = 0

    for i in range(n + 1):
        for j in range(m + 1):
            if i + j == len(c):
                continue  # We've already placed all chars of c

            # If we can take the next char from a (i.e. i < n), update dp[i+1][j]
            if i < n:
                # Cost is 0 if c[i+j] matches a[i], else 1
                cost = 0 if c[i + j] == a[i] else 1
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + cost)

            # If we can take the next char from b (i.e. j < m), update dp[i][j+1]
            if j < m:
                # Cost is 0 if c[i+j] matches b[j], else 1
                cost = 0 if c[i + j] == b[j] else 1
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + cost)

    # dp[n][m] is the minimum changes needed to match all of c with all of a and b
    print(dp[n][m])


# Reading multiple test cases
t = int(input().strip())
for y in range(t):
    solve()
