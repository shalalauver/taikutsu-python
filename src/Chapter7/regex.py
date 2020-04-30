#!/usr/bin/env python3
import re

#7.2.1 正規表現を用いてテキストパターンを検索する
#7.2.2 Regexオブジェクトとマッチする
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search('私の電話番号は415-555-4242です．')
print(">>>phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')")
print(">>>mo = phone_num_regex.search('私の電話番号は415-555-4242です．')")
print('電話番号が見つかりました：' + mo.group())

print("\n=====================================================================\n")
#7.3.1 丸カッコを用いたグルーピング

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

print(">>>phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')")
print(">>>mo = phone_num_regex.search('私の電話番号は415-555-4242です．')")
mo = phone_num_regex.search('私の電話番号は415-555-4242です．')
print(">>>mo.group(1)\n", mo.group(1))
print(">>>mo.group(2)\n", mo.group(2))
print(">>>mo.group(0)\n", mo.group(0))
print(">>>mo.group()\n", mo.group())

area_code, main_number = mo.groups()

print('area_code, main_numberと分けることもできる．')
print("area_code, main_number = mo.groups()")

print('area_code = ', area_code)
print('main_number = ', main_number)


print("\n=====================================================================\n")
#7.3.2 縦線を使って複数のグループとマッチする
print(">>>hero_regex = re.compile(r'Batman | Tina Fey')")
print(">>>mo1 = hero_regex.search('Batman and Tina Fey')")
hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey')
print(">>>mo1.group()\n", mo1.group())
print(">>>mo2 = hero_regex.search('Tina Fey and Batman.')")
mo2 = hero_regex.search('Tina Fey and Batman.')
print('>>>mo2.group()\n', mo2.group())


print("\n=====================================================================\n")

#7.3.3 疑問符を用いた任意のマッチング
bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('The Adventure of Batman')
print("bat_regex = re.compile(r'Bat(wo)?man')")
print("mo1 = bat_regex.search('The Adventure of Batman')")
print('>>>mo1.group()\n', mo1.group())

print("mo2 = bat_regex.search('The Adventure of Batwoman')")
mo2 = bat_regex.search('The Adventure of Batwoman')
print('>>>mo2.group()\n', mo2.group())

print('\n')
print(">>>phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')")
print(">>>mo1 = phone_regex.search('私の電話番号は415-555-4242です．')")
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phone_regex.search('私の電話番号は415-555-4242です．')
print('>>>mo1.group()\n', mo1.group())
print(">>>m2 = phone_regex.search('私の電話番号は555-4242です．')")
mo2 = phone_regex.search('私の電話番号は555-4242です．')
print('>>>mo2.group()\n', mo2.group())



print("\n=====================================================================\n")

#7.3.4アスタリスクを用いた0回以上のマッチ

print("bat_regex = re.compile(r'Bat(wo)*man')")
print("mo1 = bat_regex.search('The Adventures of Batman')")
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The Adventures of Batman')
print('>>>mo1.group()\n', mo1.group())

print("mo2 = bat_regex.search('The Adventures of Batwoman')")
mo2 = bat_regex.search('The Adventures of Batwoman')
print('>>>mo2.group()\n', mo2.group())

print("mo3 = bat_regex.search('The Adventures of Batwowowoman')")
mo3 = bat_regex.search('The Adventures of Batwowowoman')
print('>>>mo3.group()\n', mo3.group())
print("\n=====================================================================\n")

#7.3.5プラスを用いた1回以上のマッチ

print("bat_regex = re.compile(r'Bat(wo)+man')")
print("mo1 = bat_regex.search('The Adventures of Batwoman')")
bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('The Adventures of Batwoman')
print('>>>mo1.group()\n', mo1.group())

print("mo2 = bat_regex.search('The Adventures of Batwowowoman')")
mo2 = bat_regex.search('The Adventures of Batwowowoman')
print('>>>mo2.group()\n', mo2.group())

print("mo3 = bat_regex.search('The Adventures of Batman')")
mo3 = bat_regex.search('The Adventures of Batman')
print('>>>mo3.group == None\n', mo3 == None)

print("\n=====================================================================\n")

#7.3.6波かっこを用いて繰り返し回数を指定する

print("ha_regex = re.compile(r'(Ha){3,5})")
print("mo1 = ha_regex.search('HaHaHaHaHa')")
ha_regex = re.compile(r'(Ha){3,5}')
mo1 = ha_regex.search('HaHaHaHaHa')
print('>>>mo1.group()\n', mo1.group())

print("mo2 = ha_regex.search('Ha')")
mo2 = ha_regex.search('Ha')
print('>>>mo2.group == None\n', mo2 == None)
