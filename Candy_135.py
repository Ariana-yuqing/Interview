def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    if len(ratings) == 0:
        return 0
    sum = 1
    last_num = 1
    dec_start = -2
    dec_end = -2
    dup = []
    min_first = 0
    for i in range(1, len(ratings), 1):
        if ratings[i] > ratings[i - 1]:
            if dec_start == -2 and dec_end == -2:
                last_num += 1
                sum += last_num
            else:
                last_num = 2
                sum += last_num
                if min_first < dec_end - dec_start - len(dup):
                    for j in range(1, dec_end - dec_start + 2 - len(dup), 1):
                        sum += j
                    for k in dup:
                        sum += dec_end - k + 1
                else:
                    sum += min_first
                    for j in range(1, dec_end - dec_start - len(dup) + 1, 1):
                        sum += j
                    for k in dup:
                        if k == dec_start:
                            sum += min_first
                        else:
                            sum += dec_end - k + 1
                dec_start = -2
                dec_end = -2
                # print(sum)

        elif ratings[i] == ratings[i - 1]:
            if dec_start == -2 and dec_end == -2:
                sum += last_num
            else:
                dec_end += 1
                dup.append(i)

        elif ratings[i] < ratings[i-1]:
            if dec_start == -2 and dec_end == -2:
                sum -= last_num
                dec_start = i-1
                dec_end = i
                min_first = last_num
            else:
                dec_end += 1

        # print('{}, {}, {}, {}'.format(dec_start, dec_end, min_first, sum))
    if dec_start != -2 and dec_end != -2:
        if min_first < dec_end - dec_start - len(dup) + 1:
            for j in range(1, dec_end - dec_start + 2 - len(dup), 1):
                print(j)
                sum += j
            for k in dup:
                sum += dec_end - k + 1
        else:
            sum += min_first
            for j in range(1, dec_end - dec_start - len(dup) + 1, 1):
                sum += j
            for k in dup:
                if k == dec_start:
                    sum += min_first
                else:
                    sum += dec_end - k + 1
    return sum


def main():
    print(candy([1, 2, 5, 4, 3, 2, 1]))  # 18
    print(candy([1, 2, 5, 1, 3, 1, 2]))  # 12
    print(candy([5, 4, 3, 2, 1, 5, 3]))  # 18
    print(candy([2, 1, 3, 4, 3, 2, 1, 5, 1]))

if __name__ == '__main__':
    main()
