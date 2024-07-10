import re
import pykakasi
from pypinyin.contrib.tone_convert import to_finals
import sys
from utils import make_pinyin_list

#usage: python3 make_finals_list.py > finals_list.txt

def make_finals_dict(pinyin_list_dict):

  finals_dict = {}

  for pin in pinyin_list_dict:

    finals = to_finals(pin)

    if finals == "":
 
      continue

    if finals in finals_dict:

      finals_dict[finals] = finals_dict[finals] + pinyin_list_dict[pin]

    else:

      finals_dict[finals] = pinyin_list_dict[pin]

  return finals_dict

pinyin_list_dict = make_pinyin_list()

finals_dict = make_finals_dict(pinyin_list_dict)

for key in finals_dict:

  print( ",".join([key] + finals_dict[key]))
