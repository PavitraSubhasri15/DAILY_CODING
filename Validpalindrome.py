class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        length=len(s)
        while i<length:
            if not s[i].isalpha() and not s[i].isdigit():
                s=s[:i]+s[i+1:]
                length-=1
                continue
            i+=1
        s=s.lower()
        l=s.split(" ")
        s="".join(l)
        return s==s[::-1]
        
