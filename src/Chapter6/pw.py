#! /usr/bin/env python3

#プロジェクト：パスワードロッカー


PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmAlvQyKAxiVH5G8v01f1MLZF3sdt',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方： python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

#最初のコマンドライン引数がアカウント名
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをコピーしました')
else:
    print(account + 'というアカウント名はありません')
