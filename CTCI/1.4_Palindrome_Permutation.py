# Tact Coa
# True: taco cat / atco cta

def palindrome_permutation(s):
    s = s.lower().replace(" ", "")
    hashtable = {}
    odd_count = 0
    for c in s:
        if c in hashtable:
            hashtable[c] += 1
        else:
            hashtable[c] = 1
        if hashtable[c] % 2 == 0:
            odd_count -= 1
        else:
            odd_count += 1

    return odd_count <= 1

# Todo bit manipulation
# def palindrome_permutation_bit(s):


    # single = False
    # for v in hashtable.values():
    #     if v % 2 != 0:
    #         if single:
    #             return False
    #         else:
    #             single = True
    # return True



def main():
    print('taco cat: {}'.format(palindrome_permutation("taco cat")))
    print('hel lo: {}'.format(palindrome_permutation("hel lo")))
    print(':{}'.format(palindrome_permutation("")))


if __name__ == '__main__':
    main()
