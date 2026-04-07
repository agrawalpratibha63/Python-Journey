###########################################################
             #Daily practice question
###########################################################

# QUES: CALCULATED DELAY ARRIVAL Time

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        res=arrivalTime+delayedTime
        if res>=24:
            return res%24
        else:
            return res
        