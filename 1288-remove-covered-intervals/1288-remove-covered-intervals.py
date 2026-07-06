class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i=1
        print(intervals)
        while i<len(intervals):
            if intervals[i][0]==intervals[i-1][0]:
                if  intervals[i][1]>=intervals[i-1][1]:
                    intervals.pop(i-1)

                else:
                    intervals.pop(i)

            if intervals[i][1]==intervals[i-1][1]:
                if  intervals[i][0]>=intervals[i-1][0]:
                    intervals.pop(i)

                else:
                    intervals.pop(i-1)


            elif intervals[i][1]<=intervals[i-1][1]:
                intervals.pop(i)

            else:
                i+=1

        return len(intervals)






        
        
      











        