import sys
import math

def gcd(a, b):
    return math.gcd(a, b)

class SegmentTree:
    def __init__(self, data, default=0, func=math.gcd):
        """Build a segment tree for `data` using `func` (GCD in this case)."""
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.default = default
        self.func = func
        self.tree = [default] * (2 * self.size)

        # Build the tree (assign leaves)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]

        # Compute internal nodes
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = func(self.tree[i << 1], self.tree[i << 1 | 1])

    def query(self, left, right):
        """Returns GCD of range [left, right] in 0-based indexing."""
        if left > right:
            return self.default
        left += self.size
        right += self.size
        res = self.default
        while left <= right:
            if left & 1:
                res = self.func(res, self.tree[left])
                left += 1
            if right % 2 == 0:
                res = self.func(res, self.tree[right])
                right -= 1
            left >>= 1
            right >>= 1
        return res

# Read all input at once for efficiency
input_data = sys.stdin.read().split()
index = 0

t = int(input_data[index])
index += 1
out = []

for _ in range(t):
    # Read n, q
    n, q = map(int, input_data[index:index+2])
    index += 2
    arr = list(map(int, input_data[index:index+n]))
    index += n

    # If n == 1, all queries output 0 (single element => infinite modulo)
    if n == 1:
        for __ in range(q):
            index += 2  # Skip the query since answer is always 0
            out.append("0")
        continue

    # Build the diff array
    diff = [abs(arr[i+1] - arr[i]) for i in range(n - 1)]

    # Build segment tree over diff array for GCD
    seg_tree = SegmentTree(diff, default=0, func=gcd)

    for __ in range(q):
        l, r = map(int, input_data[index:index+2])
        index += 2
        l -= 1  # Convert to 0-based index
        r -= 1  # Convert to 0-based index

        if l == r:
            # Single element => any m works => output 0
            out.append("0")
        else:
            # Query GCD on range [l, r-1] in diff array
            Gcd = seg_tree.query(l, r-1)
            out.append(str(Gcd))

# Print all output at once for efficiency
sys.stdout.write("\n".join(out) + "\n")
