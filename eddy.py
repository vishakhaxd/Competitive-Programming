import math
import heapq
import sys


def prim(points):
    n = len(points)
    visited = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0  # Start from point 0
    heap = [(0, 0)]  # (cost, point_index)
    total_cost = 0.0

    while heap:
        cost, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost

        for v in range(n):
            if not visited[v]:
                dist = math.hypot(points[u][0] - points[v][0], points[u][1] - points[v][1])
                if dist < min_edge[v]:
                    min_edge[v] = dist
                    heapq.heappush(heap, (dist, v))

    return total_cost


def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while idx < len(input_lines):
        if input_lines[idx].strip() == '':
            idx += 1
            continue
        n = int(input_lines[idx])
        idx += 1
        points = []
        for _ in range(n):
            x, y = map(float, input_lines[idx].split())
            points.append((x, y))
            idx += 1
        ans = prim(points)
        print(f"{ans:.2f}")


if __name__ == "__main__":
    main()
