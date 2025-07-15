def solve():
    s = list(input().strip())  # Convert string to list for mutability
    n = len(s)

    for i in range(1, n):
        j, curr = i - 1, i
        while j >= 0 and s[curr] > '0' and s[curr] > chr(ord(s[j]) + 1):
            s[curr] = chr(ord(s[curr]) - 1)  # Decrease digit
            s[curr], s[j] = s[j], s[curr]  # Swap
            curr -= 1
            j = curr - 1

    print("".join(s))

# Handling multiple test cases
t = int(input())
for _ in range(t):
    solve()
