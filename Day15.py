##############################################################
                    #Day15 practice question
##############################################################

#ques Add binary digits.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1=int(a,2)
        a2=int(b,2)
        s=a1+a2
        s1=bin(s)[2:]
        return s1