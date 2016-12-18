class DataEntry:
    time = None
    count = 0
    type = None

    def __init__(self, time, count, type):
        self.time = time
        self.count = count
        self.type = type


def merge_sort(data):
    n = len(data)
    if n == 0 or n == 1:
        return data
    left = merge_sort(data[0: int(n/2)])
    right = merge_sort(data[int(n/2):])
    return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i].time < right[j].time:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def cal(num, dataPoint):
    if dataPoint.type == 'enter':
        return num + dataPoint.count, dataPoint.time
    else:
        return num - dataPoint.count, dataPoint.time


def find_busiest_time(data):
    if len(data) == 0:
        return None

    data = merge_sort(data)

    max_num = 0
    max_ts = data[0].time
    max_ts2 = data[0].time
    lastTimestamp = data[0].time
    last_num = 0
    for ind, v in enumerate(data):
        if v.time == lastTimestamp and max_ts == lastTimestamp:
            max_num, max_ts = cal(max_num, v)
            max_ts2 = data[ind+1].time

        last_num, lastTimestamp = cal(last_num, v)
        if last_num > max_num:
            max_num = last_num
            max_ts = lastTimestamp
            max_ts2 = data[ind + 1].time
    return max_ts, max_ts2


def main():
    l1 = DataEntry(1, 1, 'enter')
    l2 = DataEntry(1, 2, 'enter')
    l3 = DataEntry(1, 1, 'exit')
    l4 = DataEntry(2, 2, 'enter')
    l5 = DataEntry(5, 2, 'exit')

    data = [l1, l5, l2, l4, l3]
    print(find_busiest_time(data))


if __name__ == '__main__':
    main()