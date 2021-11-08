# leetcode-solutions

To the extent possible under law, [Michael Rodriguez](https://github.com/kaichiuchu)
has waived all copyright and related or neighboring rights to leetcode-solutions.

## Introduction

This repository hosts an ongoing effort to produce solutions to LeetCode
problems with detailed explanations, benchmarks, and unit tests.

## Structure

Neither the solutions, nor tests, nor benchmarks make use of any code outside
of the Python standard library or any of its native features.

For each problem solved, there exists a unit test for each problem, for each
solution and a benchmark for each solution. All of the solutions and benchmarks
are contained within the `solutions` directory.

## Benchmarking

For example, if you want to run the benchmark for the Two Sum problem, nagivate
to the `solutions/two_sum` directory and execute `benchmark.py`.

## Testing

`python -m unittest` will run all of the test cases for each problem, for each
solution. This command should be executed in the root directory of this
project.

If you wish to execute only one unit test, navigate to the `tests` directory
and run the appropriate script. All of the scripts will have this format:

`test_short_problem_name_here.py`

For example, if you wish to run the unit test for the Two Sum problem, navigate
to the `tests` directory and execute `test_two_sum.py`.

The tests use the same test case data contained on LeetCode for each problem.
