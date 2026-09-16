import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOLUTION = ROOT / "solution.py"


def run_case(input_text):
    completed = subprocess.run(
        [sys.executable, str(SOLUTION)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip().splitlines()


class MinimumOperationsTests(unittest.TestCase):
    def test_sample_case(self):
        self.assertEqual(
            run_case("2\n1\n-2\n2\n1 -1\n"),
            ["2", "-1"],
        )

    def test_already_zero(self):
        self.assertEqual(run_case("1\n3\n0 0 0\n"), ["0"])

    def test_positive_total_is_impossible(self):
        self.assertEqual(run_case("1\n2\n1 0\n"), ["-1"])

    def test_negative_values_with_enough_operations(self):
        self.assertEqual(run_case("1\n2\n-1 -1\n"), ["2"])
        self.assertEqual(run_case("1\n2\n-2 1\n"), ["1"])

    def test_insufficient_operations_for_negative_entries(self):
        self.assertEqual(run_case("1\n3\n-1 1 0\n"), ["-1"])


if __name__ == "__main__":
    unittest.main()
