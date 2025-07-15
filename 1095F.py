import sys


def get_leader(x, parent):
    if x == parent[x]:
        return x
    parent[x] = get_leader(parent[x], parent)
    return parent[x]


def merge(x, y, parent):
    x = get_leader(x, parent)
    y = get_leader(y, parent)
    if x == y:
        return False
    parent[x] = y
    return True



n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((w, u - 1, v - 1))

z = min(range(n), key=lambda i: a[i])
for i in range(n):
    if i != z:
        edges.append((a[i] + a[z], i, z))

edges.sort()

parent = list(range(n))
ans = 0

for w, u, v in edges:
    if merge(u, v, parent):
        ans += w

print(ans)


