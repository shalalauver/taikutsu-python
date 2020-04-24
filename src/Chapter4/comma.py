spam = ['apples', 'bananas', 'tofu', 'cats']
spam = [1, 2, 3]
print(spam)
def plusAdd(list):
    andchar = str(list[0])
    for i in range(1, len(list) - 1):
        andchar = andchar + ', ' + str(list[i])
    return andchar + ', and ' + str(list[-1])

if __name__ == '__main__':
    print(plusAdd(spam))
