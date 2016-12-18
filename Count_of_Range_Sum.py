def countRangeSum(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """

    def sort(arr):
        global count
        mid = int(len(arr) / 2)
        if mid == 0:
            return arr
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        result = []

        t = 0
        for i in range(len(left)):
            j, k = 0, 0
            # print('{}, {}'.format(j, len(right)))
            # print('i: {}, {}'.format(i, len(left)))
            while j < len(right) and right[j] - left[i] < lower:
                j += 1
            while k < len(right) and right[k] - left[i] <= upper:
                k += 1
            while t < len(right) and right[t] < left[i]:
                result.append(right[t])
                t += 1
            count += k - j
            result.append(left[i])
        while t < len(right):
            result.append(right[t])
            t += 1
        return result

    if not nums:
        return 0
    global count
    count = 0
    sums = [nums[0]] * len(nums)
    if sums[0] >= lower and sums[0] <= upper:
        count += 1

    for i in range(len(nums) - 1):
        sums[i + 1] = sums[i] + nums[i + 1]
        if sums[i + 1] >= lower and sums[i + 1] <= upper:
            count += 1

    sort(sums)
    return count


def main():
    print(countRangeSum([0, -1, 1, 2, -3, -3], -3, 1))


if __name__ == '__main__':
    main()