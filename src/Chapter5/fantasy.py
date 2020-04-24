item = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '矢': 12}

def display_inventory(dict):
    print('持ち物リスト：')
    total_items = 0
    for k, v in item.items():
        print(str(v) + ': ' + str(k))
        total_items += v
    print('アイテム総数：' + str(total_items))


if __name__ == '__main__':
    display_inventory(item)
