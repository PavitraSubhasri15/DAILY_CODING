#User function Template for python3
import math
class Solution:
    
    def largestPrimeFactor(self,n):
        # Step 1: Remove factors of 2
        while n % 2 == 0:
            last_factor = 2
            n //= 2
    
        # Step 2: Try odd factors up to sqrt(n)
        factor = 3
        while factor * factor <= n:
            while n % factor == 0:
                last_factor = factor
                n //= factor
            factor += 2
    
        # Step 3: If n > 2, it’s a prime
        if n > 2:
            last_factor = n
    
        return last_factor

                        
                    
        
        
        
