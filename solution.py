import sys


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    answers = []

    for _ in range(t):
        n = data[pos]
        pos += 1
        arr = data[pos:pos + n]
        pos += n

        total = sum(arr)

        # Every operation increases the total sum by exactly 1.
        # Therefore, the number of operations must be -total.
        if total > 0:
            answers.append("-1")
            continue

        operations = -total

        # For Ai < 0, at least ceil(-Ai / 2) operations must choose
        # index i as the index receiving +2.
        required_plus_operations = sum(
            (-value + 1) // 2 for value in arr if value < 0
        )

        if required_plus_operations <= operations:
            answers.append(str(operations))
        else:
            answers.append("-1")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()
