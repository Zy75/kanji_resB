import sqlite3
import re
from pypinyin.contrib.tone_convert import to_finals

def make_kanji_list():

  with open('kanji_table.txt') as f:

    kanji_list_br = f.readlines()

  kanji_list = []

  for kanji_info_br in kanji_list_br:

    kanji_info_c = kanji_info_br.strip()

    kanji_info = kanji_info_c.split()

    kanji_list.append(kanji_info)

  return kanji_list 

def compute_sum(dict):

  return sum(map(lambda x: float(x[1][0]) ,dict.items()))

def make_finals_dict():

  with open('finals_list.txt') as f:

    finals_list_br = f.readlines()

  finals_dict = {}

  for finals_line_br in finals_list_br:

    finals_line = finals_line_br.strip()

    finals_list = finals_line.split(",")

    finals = finals_list[0]
    spins = finals_list[1:]

    finals_dict[finals] = spins

  return finals_dict

def check_vowel(char):
        
  if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    return True
  else:
    return False

# yomi_finals : latter part of onyomi which is removed of consonants. 7/5:'y' also removed.

def get_onyomi_finals(roman_yomi):

  if check_vowel(roman_yomi[0]) == False:
    if check_vowel(roman_yomi[1]) == False:
      if check_vowel(roman_yomi[2]) == False:
        if check_vowel(roman_yomi[3]) == False:
          yomi_finals = roman_yomi[4:]
        else:
          yomi_finals = roman_yomi[3:]
      else:
        yomi_finals = roman_yomi[2:]
    else:
      yomi_finals = roman_yomi[1:]
  else:
    yomi_finals = roman_yomi[0:]

  return yomi_finals

def group_by_onyomi_finals(all_list,kks):

  dict = {}

  for kanji_yomi in all_list:

    first = True

    for k_yomi in kanji_yomi:

      if first == True:

        kanji = k_yomi

        first = False

      else:

        yomi = k_yomi

        roman_yomi = kks.convert(yomi)[0]['kunrei']


        yomi_finals = get_onyomi_finals(roman_yomi)

        if yomi_finals in dict:

          dict[yomi_finals].append(kanji)

        else:
          dict[yomi_finals] = [kanji]

  for key in dict:

    dict[key] = remove_duplicates(dict[key])
    
  return dict

def sort_with_frequency(dict):
 
  new_dict = {}
 
  for key in dict:

    new_dict[key] = [ len(dict[key]) , dict[key] ]

  tuple = sorted(new_dict.items(), key=lambda x:x[1], reverse=True)

  new_dict = {x:y for x,y in tuple}

  return new_dict

def make_pinyin_list():

  with open('pinyin_table_u.txt') as f:
    pinyin_list_br = f.readlines()

  dict = {}

  for pinyin_pair_br in pinyin_list_br:

    pinyin_pair = pinyin_pair_br.strip()

    spin,pin = pinyin_pair.split()

    if pin in dict:
      
      dict[pin].append(spin)

    else:
 
      dict[pin] = [spin]

  return dict

def make_school_onyomi_list():

  with open('joyo_onyomi_school.txt') as f:
    school_on_br = f.readlines()

  school_on = []

  for kanji_br in school_on_br:

    kanji = kanji_br.strip()

    kanji_split = kanji.split(",")

    school_on.append(kanji_split)

  return school_on

def make_variant_list():
  
  with open('joyo-variants.txt') as f:
    joyo_v_br  = f.readlines()

  joyo_v = []
  for kanji_br in joyo_v_br:
  
    kanji = kanji_br.strip()

    kanji_sp = kanji.split(",")

    if len(kanji_sp) == 3: 
      if kanji_sp[1] == 'joyo/variant':
     
        joyo_v.append([kanji_sp[0],kanji_sp[2]])

  return joyo_v

def remove_duplicates(list_in):
 
# also removes empty lists.
 
  result = []
  [result.append(x) for x in list_in if ( x not in result ) and ( not x == [] )]

  return result 

def group_by_yomi(all_list):

  dict = {}

  for kanji_yomi in all_list:

    first = True

    for k_yomi in kanji_yomi:

      if first == True:

        kanji = k_yomi

        first = False

      else:

        yomi = k_yomi        
      
        if yomi in dict:

          dict[yomi].append(kanji)

        else:

          dict[yomi] = [kanji]

  for key in dict:

    dict[key] = remove_duplicates(dict[key])

  return dict
