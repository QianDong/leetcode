import numpy as np
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        word1 = list(word1)
        word2 = list(word2)
        if len(word1) != len(word2):   # if two words has different length, return false
            return False
        if set(word1) != set(word2):   # # if two words has different characters, return false
            return False
        # the frequency of the two words should be "the same", even the frequency are for different chars
        # f.x. 'abbcccdddd' with the frequency[1,2,3,4] is close to 'fffjkkkkgg' with the frequency [3,1,4,2]
        uniq_char1, counts_char1 = np.unique(word1, return_counts=True)
        uniq_char2, counts_char2 = np.unique(word2, return_counts=True)
        if sorted(counts_char1) != sorted(counts_char2):
            return False
        else:
            return True

#mySolution = Solution()        
#mySolution.closeStrings(word1,word2)     
        
