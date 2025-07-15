def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    graph = [list(map(int, list(input().strip()))) for _ in range(n)]
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j]:
                dist[i][j] = 1

    floyd_warshall(n, dist)

    m = int(input())
    path = list(map(lambda x: int(x) - 1, input().split()))

    compressed = [path[0]]
    last_index = 0
    for i in range(1, m):
        last_node = path[last_index]
        if dist[last_node][path[i]] < i - last_index:
            #############
            compressed.append(path[i - 1])
            last_index = i - 1
    compressed.append(path[-1])

    print(len(compressed))
    print(' '.join(str(x + 1) for x in compressed))

if __name__ == "__main__":
    main()
