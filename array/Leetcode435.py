def eraseOverlapIntervals(intervals):

    if not intervals:
        return 0
    
    intervals.sort(key=lambda x : x[-1]) #[[1,2],[1,3],[2,3],[3,4]]

    noOverLap = []
    jump = 0

    for interval in intervals:
        if not noOverLap or noOverLap[-1][1] <= interval[0]:
            noOverLap.append(interval)
        else:
            jump += 1


    return jump



intervals = [[1,100],[11,22],[1,11],[2,12]]

res = eraseOverlapIntervals(intervals)
print(res)

