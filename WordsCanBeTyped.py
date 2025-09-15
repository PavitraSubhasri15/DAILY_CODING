QUESTION:
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

 

Example 1:

Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.



class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split()
        d={}
        for word in l:
            d[word]=d.get(word,0)+1
        for word in l:
            for ch in brokenLetters:
                if ch in word:
                    if d[word]==0:
                        continue
                    else:
                        d[word]-=1
        return sum(d.values())
                
             


        
