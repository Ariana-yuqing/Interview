def is_unique_1(s):
    hashset = set()
    for c in s:
        if c in hashset:
            return False
        else:
            hashset.add(c)
    return True


def is_unique_2(s):
    char_set = [False] * 128
    for c in s:
        c_value = ord(c)
        if char_set[c_value]:
            return False
        else:
            char_set[c_value] = True
    return True

# Todo: use no additional memory


def main():
    print('hello: ' + str(is_unique_1("hello")))
    print('abcdefg: ' + str(is_unique_1("abcdefg")))
    print('hello: ' + str(is_unique_2("hello")))
    print('abcdefg: ' + str(is_unique_2("abcdefg")))

if __name__ == '__main__':
    main()

