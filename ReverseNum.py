def reverse_num(num):
    reverse = 0
    while num > 0:
        reverse = (reverse * 10) + (num % 10)
        num = num // 10
    return reverse


if __name__ == '__main__':
    print(reverse_num(20))
