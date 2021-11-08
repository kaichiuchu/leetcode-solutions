#!/usr/bin/env python
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

import timeit

if __name__ == '__main__':
    bruteforce_solution_result = timeit.timeit(setup='import solution',
                                               stmt='solution.BruteForceSolution([2,7,11,15], 9)')

    print(
        f'Brute force solution took {int(bruteforce_solution_result*1000)}ms.')

    dict_solution_result = timeit.timeit(setup='import solution',
                                         stmt='solution.DictSolution([2,7,11,15], 9)')

    print(f'Dictionary solution took {int(dict_solution_result*1000)}ms.')
