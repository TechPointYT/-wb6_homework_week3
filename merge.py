class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        self.quickSort(intervals, 0, len(intervals) - 1)
        res = [intervals[0]]
        i = 1
        
        while i < len(intervals):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(intervals[i][1],res[-1][1])
            else:
                res.append(intervals[i])
            i+=1
            
        return res
    
    
    def quickSort(self, intervals, s, e):
        if s >= e:
            return 
        parI = self.partition(intervals, s, e )
        self.quickSort(intervals, s, parI - 1)
        self.quickSort(intervals, parI + 1, e )
        
    def partition(self, intervals, s, e):
        
        pivot = intervals[e]
        parI = s
        for i in range(s, e):
            if intervals[i][0] <= pivot[0]:
                temp = intervals[i]
                intervals[i] = intervals[parI]
                intervals[parI] = temp
                parI += 1 
        temp = intervals[parI]
        intervals[parI] = intervals[e]
        intervals[e] = temp
        return parI
