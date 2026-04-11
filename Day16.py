#################################################################
                     #Day16 Practice
#################################################################

#Counting Bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        lis=[]
        for i in range(n+1):
            m=bin(i)[2:]
            sum1=0
            for i in m:
                sum1+=int(i)
            lis.append(sum1)
        return lis