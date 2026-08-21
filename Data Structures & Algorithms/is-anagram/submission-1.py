class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrayS = list(s)
        arrayT = list(t)

        compArr = [0] *26

        for i in arrayS:
            compArr[ord(i)-ord('a')]+=1

        for i in arrayT:
            compArr[ord(i)-ord('a')]-=1

        for i in compArr:
            if i != 0:
                return False
        
        return True

        
        