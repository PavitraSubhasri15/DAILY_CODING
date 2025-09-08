QUESTION:
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them

CODE:
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1,n):
            b=n-a
            if "0" not in str(a) and "0" not in str(b):
                return [a,b]
