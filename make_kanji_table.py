import sqlite3
import sys
from utils import make_school_onyomi_list,make_variant_list,make_pinyin_list

#usage: python3 make_kanji_table.py > kanji_table.txt

def valid_spin(spin,pinyin_list_dict):

  for pin in pinyin_list_dict:

    if spin in pinyin_list_dict[pin]:

      return True

  return False

school_on = make_school_onyomi_list()
joyo_v = make_variant_list()

pinyin_list_dict = make_pinyin_list()

conn = sqlite3.connect('Unihan.sl3')
cur = conn.cursor()

def get_unicode(kanji):

  return format(ord(kanji),'04X')

def get_variant(kanji,joyo_v):

  for kanji_pair in joyo_v:

    kanji_jp = kanji_pair[0]
    kanji_v = kanji_pair[1]

    if kanji_jp == kanji:

      return kanji_v

  return None

def get_spin(kanji):

  unicode = get_unicode(kanji)

  cur.execute('select v from kMandarin where k="U+' + unicode + '"')
  
  result = cur.fetchall()

  if not result == []:

# take the first pinyin of kMandarin. According to the document, the second is for Taiwan if exists.
    return result[0][0]
 
  else:

    return None  

error_list = []

for kanji_yomi in school_on:

  kanji = kanji_yomi[0]
  yomi = kanji_yomi[1:]

  spin = get_spin(kanji) 

  kanji_var = get_variant(kanji,joyo_v)
 
  if not kanji_var == None:
    
    spin_var = get_spin(kanji_var)    

  else:

    spin_var = None
 
  if spin_var == None:

    spin_out = spin
 
  else:  

    spin_out = spin_var

  if not valid_spin(spin_out,pinyin_list_dict):

    error_list.append([kanji,spin_out])

  print(" ".join( [kanji,spin_out] + yomi ))

#print(error_list)

cur.close()
conn.close()
