# def string_compression(s):
#     count = 0
#     table = [0] * 52
#     for c in s:
#         v = getValue(c)
#         if table[v] == 0:
#             count += 1
#         table[v] += 1
#
#     res = ""
#     if count * 2 < len(s):
#         for i in range(52):
#             if table[i] > 0:
#                 res += getChar(i) + str(table[i])
#         return res
#     else:
#         return s


def string_compression(s):
    n = len(s)
    i = 0
    res = ""
    length = 0
    while i < n:
        j = i + 1
        count = 1
        while j < n and s[j] == s[i]:
            j += 1
            count += 1
        res += s[i] + str(count)
        length += 2
        i = j
    if length > n:
        return s
    else:
        return res


def getValue(c):
    v = ord(c)
    if v > 96:
        return v - ord('a') + 26
    else:

        return v - ord('A')


def getChar(v):
    if v > 25:
        return chr(v - 26 + ord('a'))
    else:
        return chr(v + ord('A'))


def main():
    s = 'aabcdefgg'
    print('{}:{}'.format(s, string_compression(s)))
    s = 'aabcccccaaa'
    print('{}:{}'.format(s, string_compression(s)))

if __name__ == '__main__':
    main()