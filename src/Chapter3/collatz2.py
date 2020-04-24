def collatz(number):
    number = int(number)
    if number%2 == 0:
        return int(number/2)
    else:
        return int(3 * number + 1)



if __name__ == '__main__':
    while True:
        try:
            num = int(input('整数を入力してください；'))
            break
        except ValueError:
            print('正しい値を入力してください！')

    while num > 1:
        num = collatz(num)
        print(num)
