import unittest

from mycd import mycd


# Run test cases
class TestMyCd(unittest.TestCase):
    test_cases = [
        ["/", "abc", "/abc"],
        ["/abc/def", "ghi", "/abc/def/ghi"],
        ["/abc/def", "..", "/abc"],
        ["/abc/def", "/abc", "/abc"],
        ["/abc/def", "/abc/klm", "/abc/klm"],
        ["/abc/def", "../..", "/"],
        ["/abc/def", "../../..", "/"],
        ["/abc/def", ".", "/abc/def"],
        ["/abc/def", "..klm", "..klm: No such file or directory"],
        ["/abc/def", "//////", "/"],
        ["/abc/def", "......", "......: No such file or directory"],
        ["/abc/def", "../gh///../klm/.", "/abc/klm"],
        ["/abc", "/.", "/"],
        ["/abc/def", "../../../123/456", "/123/456"],
        ["/abc/def", "../../../123/../456", "/456"],
        ["/abc/def", "../../../123/.../456", "...: No such file or directory"],
    ]

    def test_mycd(self):
        for src, target, expected_result in self.test_cases:
            self.assertEqual(expected_result, mycd(src, target))


if __name__ == "__main__":
    unittest.main()
