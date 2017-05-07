import heapq

arry = [2,7,3,5,2]

res = []
maxHeap = []
minHeap = []

for n in arry:
    # push
    if len(minHeap) == 0 or n >= minHeap[0]:
        heapq.heappush(minHeap,n)
    else:
        heapq.heappush(maxHeap,-n)
    # adjust
    if len(minHeap) > len(maxHeap) + 1:
        t = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, -t)
    elif len(maxHeap) > len(minHeap):
        t = heapq.heappop(maxHeap)
        heapq.heappush(minHeap, -t)
    # get median
    if len(minHeap) > len(maxHeap): # median is the smaller one
        res.append(minHeap[0])
    else:
        res.append(-maxHeap[0])

print res
