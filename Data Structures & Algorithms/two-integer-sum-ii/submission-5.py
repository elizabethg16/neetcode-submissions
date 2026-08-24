class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numGroup = dict(zip(numbers,numbers))

        for i in range(len(numbers)):
            seekVal = target - numbers[i]
            if (seekVal in numGroup) and (numbers.index(seekVal)!=i):
                if i < numbers.index(seekVal):
                    return [i+1, numbers.index(seekVal)+1]
                else:
                    return [numbers.index(seekVal)+1, i+1]
            