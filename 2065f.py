import sys
import math
from collections import defaultdict


def amin(a, b):
    return min(a, b)


def amax(a, b):
    return max(a, b)


class LCA:
    def __init__(self, n, adj, depth, euler, first):
        self.n = n
        self.adj = adj
        self.depth = depth
        self.euler = euler
        self.first = first
        self.timer = 0
        self.spt = []
        self.log = []

    def dfs(self, node, parent):
        self.first[node] = self.timer
        self.euler.append(node)
        self.timer += 1
        for neighbor in self.adj[node]:
            if neighbor == parent:
                continue
            self.depth[neighbor] = self.depth[node] + 1
            self.dfs(neighbor, node)
            self.euler.append(node)
            self.timer += 1

    def build_sparse_table(self):
        m = len(self.euler)
        self.spt = [[(0, 0)] * (math.ceil(math.log2(m)) + 1) for _ in range(m)]
        self.log = [0] * (m + 1)
        for i in range(2, m + 1):
            self.log[i] = self.log[i // 2] + 1

        for i in range(m):
            self.spt[i][0] = (self.depth[self.euler[i]], self.euler[i])

        j = 1
        while (1 << j) <= m:
            i = 0
            while i + (1 << j) - 1 < m:
                self.spt[i][j] = min(self.spt[i][j - 1], self.spt[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def lca(self, u, v):
        l, r = self.first[u], self.first[v]
        if l > r:
            l, r = r, l
        j = self.log[r - l + 1]
        return min(self.spt[l][j], self.spt[r - (1 << j) + 1][j])[1]


def solve():
    input_data = sys.stdin.read().split()
    index = 0
    tt = int(input_data[index])
    index += 1
    output = []

    for _ in range(tt):
        n = int(input_data[index])
        index += 1
        a = list(map(int, input_data[index:index + n]))
        index += n

        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = map(int, (input_data[index], input_data[index + 1]))
            index += 2
            adj[u].append(v)
            adj[v].append(u)

        # Prepare LCA
        depth = [0] * (n + 1)
        euler, first = [], [-1] * (n + 1)
        lca_solver = LCA(n, adj, depth, euler, first)
        lca_solver.dfs(1, 0)
        lca_solver.build_sparse_table()

        v = defaultdict(list)
        for i in range(1, n + 1):
            v[a[i - 1]].append(i)

        ans_str = []
        for i in range(1, n + 1):
            stack = []
            ans = float('-inf')
            dp = [0] * (n + 1)

            for node in sorted(v[i], key=lambda x: lca_solver.first[x]):
                dp[node] = 1
                if stack:
                    while stack and depth[lca_solver.lca(stack[-1], node)] < depth[stack[-1]]:
                        z = stack.pop()
                        if not stack or depth[stack[-1]] < depth[lca_solver.lca(z, node)]:
                            dp[lca_solver.lca(z, node)] = 1 if a[lca_solver.lca(z, node) - 1] == i else -1
                            stack.append(lca_solver.lca(z, node))
                        ans = amax(ans, dp[stack[-1]] + dp[z] - (depth[z] - depth[stack[-1]] - 1))
                        dp[stack[-1]] = amax(dp[stack[-1]], dp[z] + (1 if a[stack[-1] - 1] == i else -1) - (
                                    depth[z] - depth[stack[-1]] - 1))
                stack.append(node)

            while len(stack) > 1:
                z = stack.pop()
                ans = amax(ans, dp[stack[-1]] + dp[z] - (depth[z] - depth[stack[-1]] - 1))
                dp[stack[-1]] = amax(dp[stack[-1]],
                                     dp[z] + (1 if a[stack[-1] - 1] == i else -1) - (depth[z] - depth[stack[-1]] - 1))

            ans_str.append("1" if ans > 0 else "0")

        output.append("".join(ans_str))

    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    solve()
