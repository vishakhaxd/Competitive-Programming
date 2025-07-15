import sys
import bisect
input = sys.stdin.read

def solve(n, q, w, queries):
    results = []
    eatable = []
    curr = w[0]
    eatable.append((curr, 1))

    for i in range(1, n):
        if curr >= w[i]:
            curr ^= w[i]
            eatable.append((curr, i + 1))
        else:
            break
    filtered = []
    for weight, count in eatable:
        if not filtered or weight > filtered[-1][0]:
            filtered.append((weight, count))

    # For each query, binary search
    for x in queries:
        l, r = 0, len(filtered) - 1
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if x >= filtered[m][0]:
                ans = filtered[m][1]
                l = m + 1
            else:
                r = m - 1
        results.append(str(ans))

    return results


def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1

    output = []

    for _ in range(t):
        n = int(data[idx])
        q = int(data[idx + 1])
        idx += 2

        w = list(map(int, data[idx:idx + n]))
        idx += n

        queries = list(map(int, data[idx:idx + q]))
        idx += q

        result = solve(n, q, w, queries)
        output.extend(result)

    print('\n'.join(output))


if __name__ == "__main__":
    main()
