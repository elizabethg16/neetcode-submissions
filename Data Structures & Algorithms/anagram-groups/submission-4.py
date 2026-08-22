class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storedWords = {};
        
        for word in strs:
            wordArr = list(word)
            wordCount = [0] * (26)

            for letter in wordArr:
                wordCount[ord(letter)-97] = wordCount[ord(letter)-97] + 1
                
            if tuple(wordCount) not in storedWords:
                storedWords[tuple(wordCount)] = []

            storedWords[tuple(wordCount)].append(word)
        
        output = list(storedWords.values())

        return output    