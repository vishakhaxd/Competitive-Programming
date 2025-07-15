def function(n,a,b):
    b0 = b[0]
    a[0] = min(b0-a[0],a[0])
    for j in range(1,n):
        temp = b0 - a[j]
        if a[j] > a[j-1] :
            if temp > a[j-1] and temp < a[j]:
                a[j]  = b0-a[j]
        else:
            if a[j] < a[j-1] and temp < a[j-1]:
                return "NO"

    return "YES"




print(function(4,[1,4,2,5],[6]))