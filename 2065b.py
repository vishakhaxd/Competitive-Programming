import sys

result = []

def function(s):
    ans =len(s)
    for i in range(1,ans):
        if s[i] ==s[i-1]:
            return 1
    return ans


t = int(input())
for _ in range(t):
    s = input().strip()
    result.append(function(s))

sys.stdout.write("\n".join(result) + "\n")