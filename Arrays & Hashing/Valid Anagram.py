class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)





solution = Solution()
result = solution.isAnagram(s="racecar", t="carrace")
print(result)