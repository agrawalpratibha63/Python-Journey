######################################################################
                 #DAY13 PRACTICE QUESTION
#######################################################################

#QUES. MAXIMUM ICECREAM BARS

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        lis=sorted(costs)
        lis1=[]
        sum1=0
        for i in range(len(lis)):
            if sum1+lis[i]<=coins:
                sum1+=lis[i]
                lis1.append(lis[i])
            else:
                break
        return len(lis1)
             
            

        