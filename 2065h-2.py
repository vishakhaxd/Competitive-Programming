import sys

MOD = 998244353
MAXN = 2 * 10**5 + 16

# Precompute powers of 2 modulo MOD
pw2 = [1] * MAXN
for i in range(1, MAXN):
    pw2[i] = (pw2[i - 1] * 2) % MOD

class FenwickTree:
    """Fenwick Tree (Binary Indexed Tree) for range sum queries"""
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.tree[idx] = (self.tree[idx] + val) % MOD
            idx += idx & -idx

    def query(self, idx):
        if idx < 0:
            return 0
        idx += 1
        ans = 0
        while idx > 0:
            ans = (ans + self.tree[idx]) % MOD
            idx -= idx & -idx
        return ans

    def range_query(self, left, right):
        if left > right:
            return 0
        return (self.query(right) - self.query(left - 1) + MOD) % MOD

def process_test_case():
    # Read input in bulk
    str_bin = list(sys.stdin.readline().strip())
    n = len(str_bin)

    # Initialize Fenwick Trees
    stFreq0, stFreq1 = FenwickTree(n), FenwickTree(n)
    st0, st1 = FenwickTree(n), FenwickTree(n)

    # Precompute values
    for i in range(n):
        pw_inv = pw2[n - 1 - i]
        pw_direct = pw2[i]
        if str_bin[i] == '0':
            stFreq0.update(i, pw_inv)
            st0.update(i, pw_direct)
        else:
            stFreq1.update(i, pw_inv)
            st1.update(i, pw_direct)

    # Compute initial answer
    ans = (pw2[n] - 1) % MOD
    acc0, acc1 = 0, 0

    for i in range(n):
        pw_inv = pw2[n - 1 - i]
        if str_bin[i] == '0':
            ans = (ans + acc1 * pw_inv) % MOD
            acc0 = (acc0 + pw2[i]) % MOD
        else:
            ans = (ans + acc0 * pw_inv) % MOD
            acc1 = (acc1 + pw2[i]) % MOD

    # Read number of queries
    Q = int(sys.stdin.readline().strip())
    queries = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
    result = []

    for at in queries:
        pw_inv = pw2[n - 1 - at]
        pw_direct = pw2[at]

        # Efficiently update answer using BIT
        ans = (ans - st1.range_query(0, at - 1) * pw_inv) % MOD if str_bin[at] == '0' else (ans - st0.range_query(0, at - 1) * pw_inv) % MOD
        ans = (ans - stFreq1.range_query(at + 1, n - 1) * pw_direct) % MOD if str_bin[at] == '0' else (ans - stFreq0.range_query(at + 1, n - 1) * pw_direct) % MOD
        ans = (ans + MOD) % MOD

        # Flip the bit and update BIT accordingly
        if str_bin[at] == '0':
            stFreq0.update(at, -pw_inv)
            st0.update(at, -pw_direct)
            str_bin[at] = '1'
            stFreq1.update(at, pw_inv)
            st1.update(at, pw_direct)
        else:
            stFreq1.update(at, -pw_inv)
            st1.update(at, -pw_direct)
            str_bin[at] = '0'
            stFreq0.update(at, pw_inv)
            st0.update(at, pw_direct)

        # Recalculate answer efficiently
        ans = (ans + st1.range_query(0, at - 1) * pw_inv) % MOD if str_bin[at] == '0' else (ans + st0.range_query(0, at - 1) * pw_inv) % MOD
        ans = (ans + stFreq1.range_query(at + 1, n - 1) * pw_direct) % MOD if str_bin[at] == '0' else (ans + stFreq0.range_query(at + 1, n - 1) * pw_direct) % MOD

        result.append(str(ans))

    # Output results efficiently
    sys.stdout.write(" ".join(result) + "\n")

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        process_test_case()

if __name__ == "__main__":
    main()
