from tabula import read_pdf
import regex
import sys

#TODO: compare with the haitohyo on Kanji Database Project on 2010

# usage: python3 extract_haitohyo_onyomi.py > joyo_onyomi_school.txt

# the lattice option makes things worse
dfs = read_pdf("onyomi_joyo_school.pdf",pages='1-50')

# first, have to make a index list pointing to where kanji and yomi columns exist.
index_list = []

for page,df in enumerate(dfs):
 
# irregular treatment, because some page include a bad column of NANs between data.
  if page == 0:
    index_list.append([0,5,11])
    continue
  elif page == 28:
    index_list.append([0,6,11])
    continue
  elif page == 38:
    index_list.append([0,5,10])
    continue
  elif page == 43:
    index_list.append([0,5,10])
    continue

  index = [0,5,10]

  if df.iat[0,6] == '漢 字' and df.iat[0,7] == '音 訓':
    index[1] = 6
  elif df.iat[0,5] == '漢 字' and df.iat[0,6] == '音 訓':
    pass
  else:
    print('Error1')  
  
  if df.iat[0,12] == '漢 字' and df.iat[0,13] == '音 訓':
    index[2] = 12
  elif df.iat[0,11] == '漢 字' and df.iat[0,12] == '音 訓':
    index[2] = 11
  elif df.iat[0,10] == '漢 字' and df.iat[0,11] == '音 訓':
    pass
  else:
    print('Error2')

  index_list.append(index)

out_list = []

top = 2
bottom = 32

# next, extract kanji and yomi.
for index,df in zip(index_list,dfs):

# left
  for r in range(top,bottom):
    out_list.append([ df.iat[ r, index[0] ], df.iat[ r, index[0] + 1 ] ])
    
# middle
  for r in range(top,bottom):
    out_list.append([ df.iat[ r, index[1] ], df.iat[ r, index[1] + 1 ] ])

# right
  for r in range(top,bottom):
    out_list.append([ df.iat[ r, index[2] ], df.iat[ r, index[2] + 1 ] ])

katakana_re = regex.compile('[\u30A1-\u30FF]+')
kanji_re = regex.compile(r'^(\p{Han}).*$')
out_list2 = []
out = ''

first = True

for entry in out_list:

  kanji = entry[0]
  yomi = entry[1]

# exclude Nan
  if not isinstance(kanji, float):

    if first == False:    
      out_list2.append(out)
    else:
      first = False

    result = kanji_re.match(kanji)

  # remove a number behind the kanji
    if result:
      out = result[1]
    else:
      print('Error3')
      sys.exit()

  if not isinstance(yomi,float):
    if katakana_re.fullmatch(yomi):
      out = out + ',' + yomi

out_list2.append(out)

for entry in out_list2:
  print(entry) 
