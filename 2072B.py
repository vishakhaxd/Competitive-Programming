def solve(n,s):
    up_count = 0
    for ch in s:
        if ch == '-':
            up_count +=1
    low_count = n - up_count
    ans = (up_count // 2) * (up_count - up_count// 2) * low_count
    print(ans)


tt = int(input().strip())
for _ in range(tt):
    n = int(input().strip())
    s = input().strip()
    solve(n,s)

