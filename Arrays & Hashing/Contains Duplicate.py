class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] == nums[y] and x != y:
                    return True

        return False



class Solution2:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = set()
        nums.sort()

        for x in nums:
            if x in hashset:
                return True
            else:
                hashset.add(x)
        return False


#10x mais rapido
class Solution3:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False

