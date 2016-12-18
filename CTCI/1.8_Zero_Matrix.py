# Leetcode 73


# First way
# Store the index of column and rows that have been zeroed out
# O(n) memory
def zero_matrix_1(matrix):
    zero_rows = set()
    zero_cols = set()
    n = len(matrix)
    m = 0 if n == 0 else len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for row in zero_rows:
        for j in range(m):
            matrix[row][j] = 0
    for col in zero_cols:
        for i in range(n):
            matrix[i][col] = 0


# O(1) memory
def zero_matrix_2(matrix):
    n = len(matrix)
    m = 0 if n == 0 else len(matrix[0])

    row_0 = False

    for j in range(m):
        if matrix[0][j] == 0:
            row_0 = True
            break
    for i in range(n):
        if matrix[i][0] == 0:
            matrix[0][0] = 0
            break

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                # print(i, j)
                matrix[i][0] = 0
                matrix[0][j] = 0
    # print(matrix)
    for i in range(1, n):
        if matrix[i][0] == 0:
            for k in range(m):
                matrix[i][k] = 0

    for j in range(m):
        if matrix[0][j] == 0:
            for k in range(n):
                matrix[k][j] = 0

    if row_0:
        for k in range(m):
            matrix[0][k] = 0
            
            
def main():
    matrix = [[0, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 0], [41, 42, 43, 44]]
    zero_matrix_1(matrix)
    print(matrix)
    matrix = [[11, 0, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35], [41, 42, 43, 0, 45], [51, 52, 53, 54, 55]]
    zero_matrix_1(matrix)
    print(matrix)
    matrix = [[11, 0, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 0, 35], [41, 42, 43, 0, 45], [51, 52, 53, 54, 55]]
    zero_matrix_1(matrix)
    print(matrix)

    print('-------------')
    matrix = [[0, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 0], [41, 42, 43, 44]]
    zero_matrix_2(matrix)
    print(matrix)
    matrix = [[11, 0, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35], [41, 42, 43, 0, 45],
              [51, 52, 53, 54, 55]]
    zero_matrix_2(matrix)
    print(matrix)
    matrix = [[11, 0, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 0, 35], [41, 42, 43, 0, 45], [51, 52, 53, 54, 55]]
    zero_matrix_2(matrix)
    print(matrix)



if __name__ == '__main__':
    main()