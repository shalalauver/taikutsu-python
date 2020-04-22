import random

def get_number(input_num):
    global rand_number



rand_number = random.randint(1, 20)

while True:
    input_num = int(input("1から20の数値を入力してください"))
    if input_num == rand_number:
        break;
    elif input_num > rand_number:
        print("大きいです")
    else:
        print("小さいです")

print("当たり！")
print("正解は", str(rand_number), "です！")
