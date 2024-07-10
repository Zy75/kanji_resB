# usage: python3 make_pinyin_table_unihan.py > pinyin_table_u.txt

import sqlite3
import re
import sys

conn = sqlite3.connect('Unihan.sl3')
cur = conn.cursor()

def make_all_pinyin(cur):

  cur.execute('select v as pinyin from kMandarin group by pinyin order by pinyin asc')

  list = cur.fetchall()

  return list

pinyin_list = make_all_pinyin(cur)

table1 = [["a","ā","á","ǎ","à"],
          ["e","ē","é","ě","è"],
          ["i","ī","í","ǐ","ì"],
          ["o","ō","ó","ǒ","ò"],
          ["u","ū","ú","ǔ","ù"],
          ["ü","ǖ","ǘ","ǚ","ǜ"],
          ["n","-","ń","ň","ǹ"],
          ["m","-","ḿ","-","-"]]
list = []

for spin_a in pinyin_list:

  spin = spin_a[0]

  tmp = spin

# remove a tone.
  for v in table1:

    tmp = tmp.replace(v[1],v[0])
    tmp = tmp.replace(v[2],v[0])
    tmp = tmp.replace(v[3],v[0])
    tmp = tmp.replace(v[4],v[0])
    
  pin = tmp
  
  if re.match(r'^[a-zA-Zü]+$',pin):
    pass
  else:
    print("check failed",spin,pin)
    sys.exit()

  list.append([spin,pin])

# sort with pin( pinyin without tone ), if the same pin, then sort with spin( pin with tone )

sorted_list = sorted(list,key=lambda x:(x[1],x[0]))  

for spin,pin in sorted_list:

  print(spin,pin)

cur.close()
conn.close()
