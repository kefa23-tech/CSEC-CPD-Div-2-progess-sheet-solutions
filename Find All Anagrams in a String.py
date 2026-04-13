from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
       
        target = Counter(p)
        window = Counter()
        anagrams = []

        if len(p) > len(s):
            return anagrams

        left = 0
        for i in range(len(p)):
            window[s[i]]+=1
            if window == target:
                anagrams.append(0)        

        for right in range(len(p),len(s)):

            window[s[right]]+=1
            window[s[left]] -=1
            if window[s[left]] == 0:
                del window[s[left]]
            if window == target:
                idx = right - len(p) + 1
                anagrams.append(idx)

            left+=1
        
        return anagrams



