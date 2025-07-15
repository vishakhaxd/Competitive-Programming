def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        x, y, a = map(int, input().split())
        cycles_complete = a // (x + y)
        rest = a - cycles_complete * (x + y)

        if rest + 0.5 > x:
            print("YES")
        else:
            print("NO")

# Run the function
solve()
