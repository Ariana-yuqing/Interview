import heapq as hq


# hq.heappush(heap, value)
# value = hq.pop(heap)
# empty = not heap
def sort_k_messed_array(arr, k):
    if not arr:
        return arr

    heap = []
    result = []
    for i in range(k + 1):
        hq.heappush(heap, arr[i])

    for j in range(k + 1, len(arr) - k, 1):
        result.append(hq.heappop(heap))
        hq.heappush(heap, arr[j])

    while heap:
        result.append(hq.heappop(heap))

    return result