# d = {0:7,1:6,2:5,3:4,4:3,5:2,6:1,7:0,8:9,9:8}
def solve(n):
    for i in range(7):
        new_n = n - i
        digits = [int(d) for d in str(new_n)]
        minimum_change = min((7 - d) % 10 for d in digits)
        if i >= minimum_change:
            return i
    return 7

# t = int(input())
t =1
results = []
for _ in range(t):
    # n = int(input())
    n= 5
    results.append(solve(n))

for res in results:
    print(res)
