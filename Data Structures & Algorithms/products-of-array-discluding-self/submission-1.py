class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * (len(nums))
        # option one: 2D array
        # option two: multiply everything, divide?
        product = 1
        zeroCount = 0
        zeroIndex = 1

        for i in nums:
            product = product * i
        
        if product != 0:
            for i in range(0, len(nums)):
                output[i] = (int)( product / nums[i] )

            return output
        else:
            product = 1
            for i in range(0, len(nums)):
                if nums[i] == 0:
                    zeroCount = zeroCount + 1
                    zeroIndex = i
                else:
                    product = product * nums[i]

            if zeroCount == 1:
                output[zeroIndex] = product
            
            return output
