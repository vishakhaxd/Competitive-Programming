import sys
import bisect


def function(n, m, a, b):
    b.sort()
    a[0] = min(a[0], b[0] - a[0])
    for i in range(1, n):
        idx = bisect.bisect_left(b, a[i] + a[i - 1])

        if idx == m:
            transformed = a[i]
        else:
            transformed = b[idx] - a[i]

        if min(a[i], transformed) >= a[i - 1]:
            a[i] = min(a[i], transformed)
        elif max(a[i], transformed) >= a[i - 1]:
            a[i] = max(a[i], transformed)
        else:
            return "NO"

    return "YES"


# Read input
t = int(input())
result = []

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    result.append(function(n, m, a, c))


sys.stdout.write("\n".join(result) + "\n")
