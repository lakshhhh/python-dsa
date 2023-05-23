#Driver Code Starts

import a
import sys

sys.setrecursionlimit(10**6)

# def run_tests(n, op):
#   tests = open("tests.txt", "r").readlines()

#   t = int(tests[0])
#   for i in range (1,t+1):
#     line = tests[i].split()
    
#     if(len(line)==0):
#       continue
#     n = int(line[0])
    
#     op = int(line[1])
#     ob = a.Solution()
#     assert ob.nthFibonacci(n) == op


import pytest

tests = open("tests.txt", "r").readlines()

@pytest.mark.parametrize("test_input, expected_output", [
    (line.split(), int(tests[i].split()[1]))
    for i, line in enumerate(tests[1:], start=1) if line.strip()
])
def test_nthFibonacci(test_input, expected_output):
    n = int(test_input[0])
    ob = a.Solution()
    assert ob.nthFibonacci(n) == expected_output