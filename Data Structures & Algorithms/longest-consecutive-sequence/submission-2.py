class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        group = {}

        for i in nums:
            group[i] = i
        
        sortedGroup = dict(sorted(group.items()))

        sortedVals = list(sortedGroup.values())
        print(sortedVals)

        if len(sortedVals) <= 1:
            return len(sortedVals)
        
        count = 1
        storedCount = 1

        for i in range(1, len(sortedVals)):
            if sortedVals[i-1] == sortedVals[i] - 1:
                count = count + 1
            else:
                if storedCount < count:
                    storedCount = count
                count = 1
        
        if storedCount < count:
                    storedCount = count

        return storedCount;
