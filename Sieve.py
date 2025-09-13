import math

class Solution:
    def sieve(self, n):
        primes=[True]*(n+1)
        primes[0]=False
        primes[1]=False
        
        for j in range(n+1):
            if primes[j]:
                for k in range(j*j,n+1,j):
                    primes[k]=False
        ans=[i for (i,val) in enumerate(primes) if val]
        return ans

