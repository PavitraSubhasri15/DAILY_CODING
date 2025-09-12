class Solution:
    def armstrongNumber (self, n):
        # code here 
        sumk=0
        number=n
        while n>0:
            digit=n%10
            sumk+=(digit**3)
            n=n//10
        return sumk==number
