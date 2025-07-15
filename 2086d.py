import sys

input = sys.stdin.read
MOD = 998244353

def bpow(x, p):
    res = 1
    while p:
        if p % 2:
            res = (res * x) % MOD
        x = (x * x) % MOD
        p //= 2
    return res


def fact(x):
    res = 1
    for i in range(1, x + 1):
        res = (res * i) % MOD
    return res


def solve_case(c):
    s = sum(c)

    dp = [0] * (s + 1)
    dp[0] = 1

    for count in c:
        if count == 0:
            continue
        for j in range(s, -1, -1):
            if j + count <= s:
                dp[j + count] = (dp[j + count] + dp[j]) % MOD

    half1 = s // 2
    half2 = (s + 1) // 2
    ans = dp[half1] * fact(half1) % MOD * fact(half2) % MOD

    for count in c:
        ans = (ans * bpow(fact(count), MOD - 2)) % MOD

    return ans


def main():
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        c = list(map(int, data[idx:idx + 26]))
        idx += 26
        results.append(solve_case(c))
    print('\n'.join(map(str, results)))


if __name__ == '__main__':
    main()
