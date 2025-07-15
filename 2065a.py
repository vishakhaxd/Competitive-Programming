import sys

res = []

def function(s):
    return s[:-2] + "i"

t = int(input())
for _ in range(t):
    s = input().strip()
    res.append(function(s))

sys.stdout.write("\n".join(res) + "\n")