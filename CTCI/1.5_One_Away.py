# brute force: recursion
def one_away(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if abs(n1 - n2) > 1:
        return False

    i, j = 0, 0
    b1, b2, b3 = False, False, False
    while i < n1 and j < n2:
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            if n1 == n2:
            # replace
                b1 = s1[i+1:] == s2[j+1:]
            elif n1 > n2:
                # delete from s2 / insert to s1
                b2 = s1[i+1:] == s2[j:]
            else:
                b3 = s1[i:] == s2[j+1:]
            return b1 or b2 or b3

    return True


def main():
    s1, s2 = "pale", "ple"
    print('{},{}:{}'.format(s1, s2, one_away(s1, s2)))
    s1, s2 = "pales", "pale"
    print('{},{}:{}'.format(s1, s2, one_away(s1, s2)))
    s1, s2 = "pales", "bales"
    print('{},{}:{}'.format(s1, s2, one_away(s1, s2)))
    s1, s2 = "pale", "bake"
    print('{},{}:{}'.format(s1, s2, one_away(s1, s2)))


if __name__ == '__main__':
    main()



