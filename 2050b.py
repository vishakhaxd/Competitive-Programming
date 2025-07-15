import sys


def transfusion(n, a):
    sum_even = 0
    sum_odd = 0
    for i in range(n):
        if i % 2 == 0:
            sum_even += a[i]
        else:
            sum_odd += a[i]
    count_odd = n // 2
    cound_even = n - count_odd
    if sum_even % cound_even == 0 and sum_odd % count_odd == 0 and sum_even / cound_even == sum_odd / count_odd:
        print("YES")
    else:
        print("NO")


input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1:index + 1 + n]))
    index += n + 1
    transfusion(n, a)
