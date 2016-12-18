# "Mr John Smith"
# "Mr%20John%20Smith"
def urlify(str, length):
    # calc the number of space first
    count = 0
    for i in range(length):
        if str[i] == ' ':
            count += 1

    i = length-1 # start from the end
    j = length + count * 2 - 1
    while i >= 0:
        if str[i] != ' ':
            str[j] = str[i]
            j -= 1
        else:
            str[j-2:j+1] = "%20"
            j -= 3
        i -= 1


def main():
    test1 = list("Mr John Smith                   ")
    test2 = list("hello world                  ")
    urlify(test1, 13)
    urlify(test2, 11)
    print('Mr John Smith: {}'.format(''.join(test1)))
    print('hello world: {}'.format(''.join(test2)))

if __name__ == '__main__':
    main()