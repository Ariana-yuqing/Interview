import heapq as hq


def kSmallestPairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    if not nums1 or not nums2:
        return []

    result = []
    h = []
    for i in range(k):
        if i >= len(nums2):
            break
        hq.heappush(h, (nums1[0] + nums2[i], 0, i))

    for j in range(k):
        if len(h) == 0:
            break
        val, col, row = hq.heappop(h)
        result.append([nums1[col], nums2[row]])
        if col + 1 < len(nums1):
            hq.heappush(h, (nums1[col + 1] + nums2[row], col + 1, row))
    return result


def main():
    print(kSmallestPairs([1, 7, 11], [2, 4, 6], 10))
    print(kSmallestPairs([1, 1, 2], [1, 2, 3], 10))


if __name__ == '__main__':
    main()