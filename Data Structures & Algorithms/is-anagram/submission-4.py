class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for l in s:
            letters[l] = letters.get(l, 0) + 1
        for l in t:
            letters[l] = letters.get(l, 0) - 1
        for v in letters.values():
            if v != 0:
                return False
        return True