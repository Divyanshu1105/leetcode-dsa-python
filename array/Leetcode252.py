def meetingRoom(intervals):
    if not intervals:
        return True
    
    intervals.sort(key=lambda x : x[0])

    current = 1
    while current < len(intervals):
        if intervals[current-1][1] > intervals[current][0]:
            return False
        current += 1

    return True


intervals = [[7,10],[2,4]]
res = meetingRoom(intervals)
print(res)