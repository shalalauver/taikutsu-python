def collatz(num):

        if num % 2 == 0:
            return num / 2
        else:
            return 3 * num + 1

try:
    input_num = int(input("整数を入力してください: "))
    while True:
        input_num = collatz(input_num)
        print(input_num)
        if input_num == 1:
            break

except ValueError:
    print("整数を入力してください")
