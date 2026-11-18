import unittest


class TestDemoFail(unittest.TestCase):
    # Demo test fixed: it failed on purpose first, now it passes.
    # This file is only on the demo/failing-test branch and is not merged.
    def test_demo_failure(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
