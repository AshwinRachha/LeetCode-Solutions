class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        dic = {"0" : "0", "1" : "1", "6" : "9", "8" : "8", "9":"6"}
        check = ''
        for n in num:
            if n not in dic:
                return False
            check += dic[n]
        return check == num[::-1]
        