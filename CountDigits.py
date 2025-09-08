QUESTION:Given a natural number n. You have to find the number of digits in it and return it.


class Solution:
    def countDigits(self, n):
    #  code here 
        count=0
        
        while n>0:
            count+=1
            n=n//10
        return count
