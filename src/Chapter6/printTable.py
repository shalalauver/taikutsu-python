#! /usr/bin/env python3
table_data = [['apples', 'oranges', 'cherries', 'banana'],
               ['Alice', 'Bob', 'Carol', 'David'],
               ['dogs', 'cats', 'mouse', 'goose']]

def print_table(tables):
    col_widths = [0] * len(tables)
    for i in range(len(tables)):
        for j in range(1, len(tables[0])):
            if col_widths[i] < len(tables[i][j]):
                col_widths[i] = len(tables[i][j])

    for i in range(len(tables[0])):
        for j in range(len(tables)):
            print(tables[j][i].rjust(col_widths[j]), end=' ')
        print("\n")

if __name__ == '__main__':
    print_table(table_data)
