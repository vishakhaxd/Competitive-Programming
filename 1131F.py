import sys
sys.setrecursionlimit(2 * 10**5)
input = sys.stdin.readline

def solve_one_case():
    n = int(input())
    adj = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # Find a leaf node (degree 1) to start
    start = next(i for i in range(1, n + 1) if len(adj[i]) == 1)

    result = []
    visited = [False] * (n + 1)

    def dfs(u):
        visited[u] = True
        result.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)

    dfs(start)

    print(' '.join(map(str, result)))

def main():
    # Codeforces usually doesn't have multiple test cases for this problem,
    # but just in case, you can wrap it this way.
    solve_one_case()

if __name__ == "__main__":
    main()
