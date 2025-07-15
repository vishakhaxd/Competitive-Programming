import sys

def function(n, m, a, b):
    b1 = b[0]

    a[0] = min(a[0], b1 - a[0])


    for i in range(1, n):
        transformed = b1 - a[i]

        if min(a[i], transformed) >= a[i - 1]:
            a[i] = min(a[i], transformed)
        elif max(a[i], transformed) >= a[i - 1]:
            a[i] = max(a[i], transformed)
        else:
            return "NO"

    return "YES"


# Read input
t = int(input())  # Number of test cases
result = []

for _ in range(t):
    n, m = map(int, input().split())  # Read n and m
    a = list(map(int, input().split()))  # Read array a
    c = list(map(int, input().split()))  # Read array b (only one value)

    # Process test case and store result
    result.append(function(n, m, a, c))

# Print all results at once
sys.stdout.write("\n".join(result) + "\n")
