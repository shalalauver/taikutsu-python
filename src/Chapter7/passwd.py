#! python3

import re


def check_psswd(pswd):
    if len(pswd) < 8:
        return False
    if not re.search(r'[a-z]', pswd):
        return False
    if not re.search(r'[A-Z]', pswd):
        return False
    if not re.search(r'[0-9]', pswd):
        return False
    
    return True


if __name__ == '__main__':
    pswd = input('パスワードを入力してください: ')
    result = check_psswd(pswd)
    if result == True:
        print('あなたのパスワードは強いです。')
    else:
        print('あなたのパスワードは弱いです。')
