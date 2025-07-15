import sys
def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = [[0] * (m + 2) for _ in range(n + 2)]
        visited = [[0] * (m + 2) for _ in range(n + 2)]
        for i in range(1, n + 1):
            s = input().strip()
            for j in range(1, m + 1):
                a[i][j] = int(s[j - 1])
                visited[i][j] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i][j] == 0:
                    break
                visited[i][j] = 1

        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if a[i][j] == 0:
                    break
                visited[i][j] = 1
        flag = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i][j] == 1 and visited[i][j] == 0:
                    flag = False
                    break
            if not flag:
                break

        print("YES" if flag else "NO")

solve()
