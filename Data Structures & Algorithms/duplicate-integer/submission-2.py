

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        min = 10^9
        max = -10^9

        for i in nums:
            if i < min:
                min = i
            if i > max:
                max = i

        size = max-min+1

        arr = [0] * size

        for i in nums:
            arr[i-min]+=1
        
        for i in arr:
            if i>1:
                return True
        
        return False
        

        