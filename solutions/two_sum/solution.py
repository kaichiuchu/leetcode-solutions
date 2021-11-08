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

def BruteForceSolution(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers `nums` and an integer `target`, return indices
    of the two numbers such that they add up to `target`.

    You may assume that each input would have exactly one solution, and you may
    not use the same element twice.

    You can return the answer in any order.
    """

    for first_index, first_num in enumerate(nums):
        for second_index, second_num in enumerate(nums[1::], start=1):
            if (first_num + second_num) == target:
                return [first_index, second_index]
    return []


def DictSolution(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers `nums` and an integer `target`, return indices
    of the two numbers such that they add up to `target`.

    You may assume that each input would have exactly one solution, and you may
    not use the same element twice.

    You can return the answer in any order.
    """

    storage = {}

    for index, num in enumerate(nums):
        diff = target - num

        if diff in storage:
            return [index, storage[diff]]

        storage[num] = index

    return []
