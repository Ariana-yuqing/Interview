def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    char_set = [0] * 128
    for c in s1:
        char_set[ord(c)] += 1

    for c in s2:
        c_value = ord(c)
        char_set[c_value] -= 1
        if char_set[c_value] < 0:
            return False

    return True


def main():
    test1 = ["abdskhe", "asklskj"]
    test2 = ["hello", "lloeh"]
    test3 = ["", "a"]
    print('test1: {}'.format(check_permutation(test1[0], test1[1])))
    print('test2: {}'.format(check_permutation(test2[0], test2[1])))
    print('test3: {}'.format(check_permutation(test3[0], test3[1])))

if __name__ == '__main__':
    main()

