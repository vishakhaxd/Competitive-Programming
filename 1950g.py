import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    g_raw = []
    w_raw = []
    pool = []

    for _ in range(n):
        g, w = input().split()
        g_raw.append(g)
        w_raw.append(w)
        pool += [g, w]

    # compress strings
    unique = sorted(set(pool))
    mp = {s: i for i, s in enumerate(unique)}
    g_id = [mp[x] for x in g_raw]
    w_id = [mp[x] for x in w_raw]

    dp = [[0] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 1

    for mask in range(1 << n):
        for last in range(n):
            if not dp[mask][last]: continue
            for nxt in range(n):
                if (mask >> nxt) & 1: continue
                if g_id[last] == g_id[nxt] or w_id[last] == w_id[nxt]:
                    dp[mask | (1 << nxt)][nxt] = 1

    res = 0
    for mask in range(1 << n):
        if any(dp[mask]):
            res = max(res, bin(mask).count("1"))

    print(n - res)


def main():
    t = input()
    if not t: return
    t = int(t)
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
