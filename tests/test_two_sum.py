# leetcode-solutions - Solutions to LeetCode problems in Python
#
# Written in 2021 by Michael Rodriguez aka kaichiuchu <mike@kaichiuchu.dev>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.

import unittest
from solutions.two_sum import solution


class TestTwoSum(unittest.TestCase):
    """Tests for the expected values from"""

    def test_dict_solution(self):
        """Tests the dictionary solution."""
        example_one = solution.DictSolution([2, 7, 11, 15], 9)
        example_two = solution.DictSolution([3, 2, 4], 6)
        example_three = solution.DictSolution([3, 3], 6)

        self.assertCountEqual(example_one, [0, 1])
        self.assertCountEqual(example_two, [1, 2])
        self.assertCountEqual(example_three, [0, 1])

    def test_brute_force_solution(self):
        example_one = solution.BruteForceSolution([2, 7, 11, 15], 9)
        example_two = solution.BruteForceSolution([3, 2, 4], 6)
        example_three = solution.BruteForceSolution([3, 3], 6)

        self.assertCountEqual(example_one, [0, 1])
        self.assertCountEqual(example_two, [1, 2])
        self.assertCountEqual(example_three, [0, 1])


if __name__ == '__main__':
    unittest.main()
