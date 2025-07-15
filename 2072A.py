def solve():
    n, k, p = map(int, input().split())

    if -n * p <= k <= n * p:
        print((abs(k) + p - 1) // p)
    else:
        print(-1)



tt = int(input())
for _ in range(tt):
    solve()

