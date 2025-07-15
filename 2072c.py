def solve():
    len_val = input().split()
    length = int(len_val[0])
    val = int(len_val[1])

    ans = [val] * length
    or_val = 0
    flag = True

    for i in range(length - 1):
        if ((or_val | i) & val) == (or_val | i):
            or_val = or_val | i
            ans[i] = i
        else:
            flag = False
            break

    if flag and (or_val | (length - 1)) == val:
        ans[length - 1] = length - 1
    for num in ans:
        print(num, end=' ')
    print()


def main():
    test_count = int(input())

    for _ in range(test_count):
        solve()


if __name__ == "__main__":
    main()
