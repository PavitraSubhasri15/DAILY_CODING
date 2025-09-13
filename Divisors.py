#User function Template for python3
import math
class Solution:
    def print_divisors(self, N):
        # code here
        ans=[]
        for i in range(1,int(math.sqrt(N))+1):
            
            if N%i==0:
                ans.append(i)
                if i!=N//i:
                    ans.append(N//i)
        ans=sorted(ans)
        for x in ans:
            print(x, end=" ")
