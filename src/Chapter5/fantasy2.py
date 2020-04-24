item = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '矢': 12}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']

def add_to_inventory(inventory, added_items):
    for loot in added_items:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1


def display_inventory(dict):
    print('持ち物リスト：')
    total_items = 0
    for k, v in dict.items():
        print(str(v) + ': ' + str(k))
        total_items += v
    print('アイテム総数：' + str(total_items))


if __name__ == '__main__':
    add_to_inventory(item, dragon_loot)
    display_inventory(item)
