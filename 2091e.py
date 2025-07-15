M = 10000001
prime = [True] * M
prime[0] = prime[1] = False
for i in range(2, int(M ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, M, i):
            prime[j] = False

def solve():
    n = int(input())
    res = 0
    for i in range(2, n + 1):
        if prime[i]:
            res += n // i
    print(res)


t = int(input())
for _ in range(t):
    solve()
