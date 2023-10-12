def is_leap_year(num):
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                return True
            else:
                return False
        return True
    return False


if __name__ == '__main__':

    value = int(input("Enter a number: "))
    if is_leap_year(value):
        print(str(value) + " is a leap year")
    else:
        print(str(value) + " is not a leap year")
