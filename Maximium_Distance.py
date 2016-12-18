#  http://algorithms.tutorialhorizon.com/given-an-array-arra-find-the-maximum-j-i-such-that-arrj-arri/

def find_max_distance(arr):
    n = len(arr)
    right_max = [[float('-inf') for _ in range(2)] for _ in range(n)]
    right_max[-1][0] = arr[-1]
    right_max[-1][1] = n-1

    for i in range(n-2, -1, -1):
        if arr[i] > right_max[i+1][0]:
            right_max[i][0] = arr[i]
            right_max[i][1] = i
        else:
            right_max[i][0] = right_max[i+1][0]
            right_max[i][1] = right_max[i+1][1]

    max_diff = 0

    l = 0
    r = 0
    while r < n and l < n:
        if right_max[r][0] > arr[l]:
            max_diff = max(right_max[r][1] - l, max_diff)
            r += 1
        else:
            l += 1
    return max_diff




def main():
    arr = [5, 2, 1, 5, 7, 8, 6, 0, 4]
    print(find_max_distance(arr))
    arr2 = [13, 3, 1, 5, 6, 4, 10, 9, 8, 0]
    print(find_max_distance(arr2))


if __name__ == '__main__':
    main()