from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #intial check for same length
            return False
        #hashmap --> freq, val: 
        countS = Counter(s)
        countT = Counter(t)

        return countS == countT
            

            




            
                

