QUESTION:Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        num=str(x)
        if num[0]=="-":
            sign=-1
            ans=int(num[:0:-1])
        else:
            ans=int(num[::-1])
        if sign==-1:
            ans*=-1
        if ans<-2**31 or ans>2**31-1:
            return 0
        else:
            return ans

        
