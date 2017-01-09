def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def merge_sort(nums):
        n = len(nums)
        mid = int(n / 2)
        if n == 0 or n == 1:
            return nums
        l = merge_sort(nums[0: mid])
        r = merge_sort(nums[mid:])
        print(l)
        print(r)
        print("---------")
        return merge(l, r)

    def merge(left, right):
        i = 0
        j = 0
        merged = []
        l_largest = [0, 0]
        last_r = -1
        if not left:
            return right
        if not right:
            return left
        # print(left)
        # print(right)
        while i < len(left) and j < len(right):
            if left[0][i] < right[0][j]:
                if left[1][i] > l_largest[1]:
                    l_largest = [left[1][i], i]
                merged.append(left[i])
                i += 1
            else:
                r_prev = right[j][2]
                if r_prev + 1 > l_largest[1] + 1:
                    right[j][1] += 1
                    right[j][2] = last_r if last_r != -1 else i
                    merged.append(right[j])
                else:
                    right[j][1] = l_largest[1] + 1
                    right[j][2] = l_largest[0]
                    merged.append(right[j])
                last_r = j
                j += 1
        return merged


    zeros = [0] * len(nums)
    table = []
    table.append(nums)
    table.append(zeros)
    table.append(zeros)
    print(table)
    res = merge_sort(table)
    # print(res)
    longest = 0
    for i in nums[:][1]:
        if i > longest:
            longest = i
    return longest

def main():
    print(lengthOfLIS([1,2,3]))

if __name__ == '__main__':
    main()