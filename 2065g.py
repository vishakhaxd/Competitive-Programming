import sys
from collections import defaultdict

def sieve(n):
    spf = list(range(n + 1))
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:  # Mark only if not already marked
                    spf[j] = i
    return spf

def get_prime_factors(x, spf):
    factors = []
    while x > 1:
        prime = spf[x]
        count = 0
        while x % prime == 0:
            x //= prime
            count += 1
        for _ in range(count):
            factors.append(prime)
    return factors

t = int(sys.stdin.readline().strip())
MAX_N = 200000
spf = sieve(MAX_N)

results = []

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    ans = 0
    one = defaultdict(int)
    two_same = defaultdict(int)
    two_diff = defaultdict(int)
    cnt = defaultdict(int)

    prime_so_far = 0

    for x in arr:
        pf = get_prime_factors(x, spf)

        if len(pf) > 2:
            continue
        if len(pf) == 1:
            one[x] += 1
            prime_so_far += 1
            ans += two_same[x] + two_diff[x] + (prime_so_far - one[x])
        elif pf[0] == pf[1]:
            two_same[pf[0]] += 1
            ans += one[pf[0]] + two_same[pf[0]]
        else:
            two_diff[pf[0]] += 1
            two_diff[pf[1]] += 1
            cnt[x] += 1
            ans += one[pf[0]] + one[pf[1]] + cnt[x]
    results.append(str(ans))

sys.stdout.write("\n".join(results) + "\n")



