def string_rotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return s2 in s1s1
    return False


def main():
    s1 = "bottlewater"
    s2 = "lewaterbott"
    print('{}, {}: {}'.format(s1, s2, string_rotation(s1, s2)))

if __name__ == '__main__':
    main()