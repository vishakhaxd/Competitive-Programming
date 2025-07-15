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

    # Compute R = (9 - S % 9) % 9
    R = (9 - (S % 9)) % 9
    for i in range(count_3+1):
        new_R = (R - 6*i)%9
        if new_R<0:
            new_R +=9
        x = (new_R*5)%9 # this is saying 2x % 9 == new_R
        if x <= count_2:
            return 'YES'
    return 'NO'

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
