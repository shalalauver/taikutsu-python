def spam(divide_by):
    try:
        return 42/divide_by
    except  ZeroDivisionError:
        print("不正な引数です")

print(spam(2))
print(spam(1))
print(spam(22))
print(spam(3))
print(spam(0))
