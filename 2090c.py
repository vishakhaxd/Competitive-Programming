T = 2000
R = 200000

Ord = []

# Equivalent of C++ Nxt(p, o)
def Nxt(p, o):
    x, y = divmod(p, T)
    if o & 1:
        y = y // 3 * 3 + 3 - y % 3
    if o & 2:
        x = x // 3 * 3 + 3 - x % 3
    return x * T + y

# Generate the Ord list (same logic as C++ code)
tp = 0
for i in range(2, T):
    if tp >= R:
        break
    if i % 3 == 2:
        for x in range(1, i, 3):
            if tp >= R:
                break
            Ord.append(x * T + i - x)
            tp += 1
    elif i % 3 == 0:
        for x in range(1, i - 1):
            if tp >= R:
                break
            if x % 3 == 1:
                Ord.append(x * T + i - x)
                tp += 1
            elif x % 3 == 2:
                Ord.append(x * T + i - x - 2)
                tp += 1
                if tp >= R:
                    break
                Ord.append(x * T + i - x)
                tp += 1
        if tp < R:
            Ord.append((i - 1) * T + 1)
            tp += 1

# Read number of test cases
t = int(input())
for _ in range(t):
    q = int(input())

    G = [set(), set()]  # G[0] and G[1] as sets of marked indices
    Ans = [0, 0]

    # Clear used positions for this test case
    for i in range(q * 4):
        if i < len(Ord):
            G[0].discard(Ord[i])
            G[1].discard(Ord[i])

    for _ in range(q):
        t_in = int(input())
        while Ans[t_in] < len(Ord) and Ord[Ans[t_in]] in G[t_in]:
            Ans[t_in] += 1

        if Ans[t_in] >= len(Ord):
            print("Error: Ran out of available Ord positions.")
            exit(1)

        t_val = Ord[Ans[t_in]]
        print(t_val // T, t_val % T)

        G[1].add(t_val)
        for o in range(4):
            G[0].add(Nxt(t_val, o))
