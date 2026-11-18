import unittest


class TestDemoFail(unittest.TestCase):
    # Deliberate demo failure: shows a failed GitHub Actions run.
    # This file is only on the demo/failing-test branch and is not merged.
    def test_demo_failure(self):
        self.assertEqual(1, 2)


if __name__ == "__main__":
    unittest.main()
