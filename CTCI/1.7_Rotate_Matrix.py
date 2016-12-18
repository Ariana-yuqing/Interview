# Leetcode: 48


def rotate_matrix(m, n):
    rotate_matrix_helper(m, n, 0)


def rotate_matrix_helper(m, n, i):
    # print(temp)
    if n == 0 or n == 1:
        return
    # print(n,i)
    end = i + n - 1
    # temp = copy.deepcopy(m[i][i:end])
    # print(temp)
    for k in range(1, n):
        temp = m[i][end-k]
        m[i][end - k] = m[i+k][i]
        m[i+k][i] = m[end][i+k]
        m[end][i+k] = m[end-k][end]
        m[end-k][end] = temp
    # print(m)
    rotate_matrix_helper(m, n - 2 , i + 1)


def main():
    m = [[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]
    rotate_matrix(m, 4)
    print(m)
    m = [[11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35], [41, 42, 43, 44, 45], [51, 52, 53, 54, 55]]
    rotate_matrix(m, 5)
    print(m)


if __name__ == '__main__':
    main()