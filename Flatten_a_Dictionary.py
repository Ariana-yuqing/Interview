def flatten_a_dictionary(dic, flat_dic, curr_key):
    if not isinstance(dic, dict):
        flat_dic[curr_key] = dic
        return
    for key in dic.keys():
        temp = curr_key
        if curr_key == '':
            curr_key = str(key)
        else:
            curr_key = curr_key + '.' + str(key)
        flatten_a_dictionary(dic[key], flat_dic, curr_key)
        curr_key = temp
    return flat_dic


def main():
    dic = {
        'Key1': '1',
        'Key2': {
            'a': '2',
            'b': '3',
            'c': {
                'd': '3',
                'e': '1'
            }
        }
    }

    output ={
        'Key1': '1',
        'Key2.a': '2',
        'Key2.b': '3',
        'Key2.c.d': '3',
        'Key2.c.e': '1'
    }

    print(flatten_a_dictionary(dic, {}, '') == output)



if __name__ == '__main__':
    main()
