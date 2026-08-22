class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s) == 0 or len(s) == 1):
            return True

        wordList = list(s.upper())
        cleanedList = []
        for i in wordList:
            if ((ord(i) >= 48 and ord(i) <= 57) or (ord(i) >= 65 and ord(i) <= 96)):
                cleanedList.append(i)
        
        checkLen = (int) (len(cleanedList)/2)
        
        for i in range(checkLen):
            if cleanedList[i] != cleanedList[len(cleanedList)-i-1]:
                return False
        
        return True