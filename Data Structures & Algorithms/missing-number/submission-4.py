class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        setNums = set(sortedNums)

        for i in range(len(sortedNums)+1):
            if i not in setNums:
                return i
        
        
