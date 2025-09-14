QUESTION:
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i]


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def devowel(word):
            return ''.join('*' if ch in vowels else ch for ch in word.lower())

        # 1. Exact words
        exact_words = set(wordlist)

        # 2. Case-insensitive map
        case_map = {}
        for word in wordlist:
            lower = word.lower()
            if lower not in case_map:
                case_map[lower] = word

        # 3. Vowel-error map
        vowel_map = {}
        for word in wordlist:
            key = devowel(word)
            if key not in vowel_map:
                vowel_map[key] = word

        ans = []
        for q in queries:
            if q in exact_words:                          # Rule 1: exact
                ans.append(q)
            elif q.lower() in case_map:                  # Rule 2: capitalization
                ans.append(case_map[q.lower()])
            elif devowel(q) in vowel_map:                # Rule 3: vowel errors
                ans.append(vowel_map[devowel(q)])
            else:                                        # Rule 4: no match
                ans.append("")
        return ans
