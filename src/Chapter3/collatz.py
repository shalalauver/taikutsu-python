def collatz(number):
    try:
        number = int(number)
        if number%2 == 0:
            return number/2
        else:
            return 3 * number + 1
    except ValueError:
        print('整数を入力してください！')
        return 'ERROR!'



if __name__ == '__main__':
    num = input('整数を入力してください：')
    while True:
        num = collatz(num)
        print(num)
        if num == 1 or num == 'ERROR!':
            break
