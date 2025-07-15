import sys

MOD = 998244353
MAXN = 2 * 10 ** 5 + 16
pw2 = [1] * MAXN
for i in range(1, MAXN):
    pw2[i] = pw2[i - 1] * 2 % MOD


class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)

    def update(self, idx, val):
        idx += self.n
        self.tree[idx] = val
        while idx > 1:
            idx //= 2
            self.tree[idx] = (self.tree[idx * 2] + self.tree[idx * 2 + 1]) % MOD

    def query(self, ql, qr):
        if ql > qr:
            return 0
        ans = 0
        ql += self.n
        qr += self.n + 1
        while ql < qr:
            if ql & 1:
                ans = (ans + self.tree[ql]) % MOD
                ql += 1
            if qr & 1:
                qr -= 1
                ans = (ans + self.tree[qr]) % MOD
            ql //= 2
            qr //= 2
        return ans


def process_test_case():
    str_bin = list(sys.stdin.readline().strip())
    n = len(str_bin)

    stFreq0, stFreq1 = SegTree(n), SegTree(n)
    st0, st1 = SegTree(n), SegTree(n)

    for i in range(n):
        if str_bin[i] == '0':
            stFreq0.update(i, pw2[n - 1 - i])
            st0.update(i, pw2[i])
        else:
            stFreq1.update(i, pw2[n - 1 - i])
            st1.update(i, pw2[i])

    ans = (pw2[n] - 1) % MOD
    acc0, acc1 = 0, 0

    for i in range(n):
        if str_bin[i] == '0':
            ans = (ans + acc1 * pw2[n - 1 - i]) % MOD
            acc0 = (acc0 + pw2[i]) % MOD
        else:
            ans = (ans + acc0 * pw2[n - 1 - i]) % MOD
            acc1 = (acc1 + pw2[i]) % MOD

    Q = int(sys.stdin.readline().strip())
    queries = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    result = []

    for at in queries:
        ans = (ans - (st1 if str_bin[at] == '0' else st0).query(0, at - 1) * pw2[n - 1 - at]) % MOD
        ans = (ans - (stFreq1 if str_bin[at] == '0' else stFreq0).query(at + 1, n - 1) * pw2[at]) % MOD
        ans = (ans + MOD) % MOD

        if str_bin[at] == '0':
            stFreq0.update(at, 0)
            st0.update(at, 0)
        else:
            stFreq1.update(at, 0)
            st1.update(at, 0)

        str_bin[at] = '1' if str_bin[at] == '0' else '0'

        if str_bin[at] == '0':
            stFreq0.update(at, pw2[n - 1 - at])
            st0.update(at, pw2[at])
        else:
            stFreq1.update(at, pw2[n - 1 - at])
            st1.update(at, pw2[at])

        ans = (ans + (st1 if str_bin[at] == '0' else st0).query(0, at - 1) * pw2[n - 1 - at]) % MOD
        ans = (ans + (stFreq1 if str_bin[at] == '0' else stFreq0).query(at + 1, n - 1) * pw2[at]) % MOD

        result.append(str(ans))

    sys.stdout.write(" ".join(result) + "\n")


def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        process_test_case()


if __name__ == "__main__":
    main()
