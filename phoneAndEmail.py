#! python3

import pyperclip
import re

phone_regex = re.compile(r'''(
  (\d{3}|\(\d{3}\))?              # 市外局番
  (\s|-|\.)?                      # 区切り
  (\d{3})                         # 3桁の番号
  (\s|-|\.)                       # 区切り
  (\d{4})                         # 4桁の番号
  (\s*(ext|x|ext.)\s*(\d{2,5}))?  # 内線番号
) ''', re.VERBOSE)

#　TODO: 電子メールの正規表現を作る。
email_regex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+
  @
  [a-zA-Z0-9.0]+
  (\.[a-zA-Z]{2,4})
) ''', re.VERBOSE)

# TODO: クリップボードのテキストを検索する

#TODO: 検索結果をクリップボードに貼り付ける
