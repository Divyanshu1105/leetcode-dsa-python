def merge(intervals):
    if not intervals:
        return intervals
    
    #always sort with the start time
    intervals.sort(key=lambda x : x[0])

    merged = []

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else: 
            merged[-1][1] = max(interval[1],merged[-1][1])
    
    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
res = merge(intervals)
print(res)