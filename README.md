# Minimum Operations to Make All Elements Zero

For an array `A`, one operation chooses indices `i` and `j`, adds `2` to `A[i]`, and subtracts `1` from `A[j]`. The goal is to make every element zero using the minimum number of operations.

## Key observations

1. Every operation increases the total array sum by exactly `1`. Therefore, the number of operations must be `-sum(A)`.
2. If `sum(A) > 0`, the task is impossible.
3. A negative element `A[i]` needs at least `ceil(-A[i] / 2)` operations in which it receives `+2`.
4. If the sum of these required operations is greater than the available number of operations, the answer is `-1`; otherwise, the required total is achievable.

## Complexity

- Time: `O(N)` per test case
- Space: `O(N)` for the input array

## Run

```bash
python3 minimum_operations.py < input.txt
```

### Sample input

```text
2
1
-2
2
1 -1
```

### Sample output

```text
2
-1
```

## Tests

Run the unit tests with:

```bash
python3 -m unittest discover -s tests -v
```

The test suite covers the sample, an already-zero array, positive total sums, feasible negative values, and impossible cases. Additional inputs are in `tests/sample_input.txt` and `tests/edge_cases_input.txt`.
