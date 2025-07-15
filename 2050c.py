def is_interesting(n):
    S = 0
    count_2 = 0
    count_3 = 0

    # Calculate initial sum and count of 2's and 3's
    for digit in n:
        d = int(digit)
        S += d
        if d == 2:
            count_2 += 1
        elif d == 3:
            count_3 += 1
    # Check possible transformations
    for k in range(count_2 + 1):
        increase_2 = 2 * k
        for i in range(count_3 + 1):
            increase_3 =6*i
            if (S+increase_2+increase_3)%9==0:
                return "YES"
    return "NO"

# Reading input
import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
results = []

for i in range(1, t + 1):
    n = data[i]
    result = is_interesting(n)
    results.append(result)

# Output results
sys.stdout.write("\n".join(results) + "\n")
