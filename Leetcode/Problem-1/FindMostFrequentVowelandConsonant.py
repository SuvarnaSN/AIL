class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Online Python compiler (interpreter) to run Python online.
        # Write Python 3 code in this online editor and run it.
        string = s
        freq , i, vowelcount, conscount = 0,0,0,0
        vowels = "aeiou"
        charCountDict = {}
        for char in string:
            if char in charCountDict:
                charCountDict[char] += 1
                
            else:
                charCountDict[char] = 1

        # print("charCountDict = "+str(charCountDict))
        charCountDictCopy = charCountDict.copy()
        vowelFound = False
        consFound = False
        while charCountDictCopy:
            maximum = max(charCountDictCopy, key = charCountDictCopy.get)
            if maximum in vowels:
                if vowelFound == False:
                    vowelFound = True
                    vowelcount = charCountDictCopy.get(maximum)
                
            else:
                if consFound == False:
                    consFound = True
                    conscount = charCountDictCopy.get(maximum)   
            del charCountDictCopy[maximum]
            
        return(vowelcount+conscount)
        