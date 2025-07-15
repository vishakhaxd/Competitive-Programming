import sys


def solve(n, edges):
    # Build adjacency list & degree array
    g = [[] for _ in range(n)]
    deg = [0] * n

    for u, v in edges:
        u -= 1
        v -= 1  # Convert to 0-based indexing
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    # Perform DFS to establish order and parent tracking
    def dfs_build_order():
        stack = [0]  # Start DFS from node 0 (arbitrary root)
        parent = [-1] * n
        order = []

        while stack:
            u = stack.pop()
            order.append(u)
            for v in g[u]:
                if v != parent[u]:  # Prevent backtracking
                    parent[v] = u
                    stack.append(v)

        return order, parent

    order, parent = dfs_build_order()

    # Postorder DP computation
    max_components = 1
    dp = [1] * n

    for u in reversed(order):  # Postorder traversal
        top1, top2 = 1, 1  # Track top 2 largest subtree contributions

        for v in g[u]:
            if v == parent[u]:  # Ignore parent node
                continue
            if dp[v] > top1:
                top1, top2 = dp[v], top1
            elif dp[v] > top2:
                top2 = dp[v]

        # Compute max removable path sum
        max_components = max(max_components, top1 + top2 + deg[u] - 2)
        dp[u] = top1 + deg[u] - 2  # Update DP value for this node

    return max_components


# Read input efficiently
def main():
    sys.setrecursionlimit(10 ** 6)  # Prevent recursion limit errors for large inputs
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])  # Number of test cases
    idx += 1
    ans = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        edges = []
        for _ in range(n - 1):
            u, v = int(data[idx]), int(data[idx + 1])
            idx += 2
            edges.append((u, v))

        ans.append(str(solve(n, edges)))

    sys.stdout.write("\n".join(ans) + "\n")


if __name__ == "__main__":
    main()
