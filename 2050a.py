import sys


def fn(m, words):
    total_length= 0
    count = 0
    for w in words:
        word_length = len(w)
        if total_length + word_length  <= m:
            total_length += word_length
            count += 1
        else:
            break
    return count

def main():
    t = int(sys.stdin.readline().strip())
    res = []
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        _ = [sys.stdin.readline().strip() for _ in range(n)]
        res.append(str(fn(m, _)))
    sys.stdout.write("\n".join(res) + "\n")


if __name__ == "__main__":
    main()

