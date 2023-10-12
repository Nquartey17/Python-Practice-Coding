import math


def armstrong_number(num):
    compare = 0;
    num_copy = num
    arr = []
    while num_copy > 0:
        arr.append(num_copy % 10)
        num_copy = num_copy // 10

    for i in range(len(arr)):
        compare = compare + int(math.pow(arr[i], len(arr)))

    if compare == num:
        return True
    return False


if __name__ == '__main__':
    print(armstrong_number(1634))
