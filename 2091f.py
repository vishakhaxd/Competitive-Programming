MOD = 998244353
MAXN = 2010


s = [''] * MAXN
dp = [[[0, 0] for _ in range(MAXN)] for _ in range(MAXN)]
sdp = [[[0, 0] for _ in range(MAXN)] for _ in range(MAXN)]

def getsum(x, y1, y2, f):
    res = sdp[x][y2][f]
    if y1 > 0:
        res -= sdp[x][y1 - 1][f]
    return res

def get(i, j, f, n, m, d):
    if s[i][j] != 'X':
        return 0
    res = 0
    if i == n - 1:
        res += 1

    if f == 0:
        res += getsum(i, max(0, j - d), min(m - 1, j + d), 1)
        res -= dp[i][j][1]

    if i < n - 1:
        res += getsum(i + 1, max(0, j - d + 1), min(m - 1, j + d - 1), 0)

    return res % MOD

def solve():
    global s, dp, sdp

    n, m, d = map(int, input().split())
    s = [input().strip() for _ in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j][0] = dp[i][j][1] = 0
            sdp[i][j][0] = sdp[i][j][1] = 0

    for i in range(n - 1, -1, -1):
        for f in [1, 0]:
            for j in range(m):
                dp[i][j][f] = get(i, j, f, n, m, d)
                sdp[i][j][f] = dp[i][j][f]
            for j in range(1, m):
                sdp[i][j][f] = (sdp[i][j][f] + sdp[i][j - 1][f]) % MOD

    ans = sum(dp[0][j][0] for j in range(m)) % MOD
    print(ans)

# Main execution
t = int(input())
for _ in range(t):
    solve()
