import sqlite3
import re
import pykakasi
from pypinyin.contrib.tone_convert import to_finals
from utils import make_finals_dict,make_kanji_list,group_by_onyomi_finals,sort_with_frequency,compute_sum,remove_duplicates
import sys

kks = pykakasi.kakasi()

finals_dict = make_finals_dict()

kanji_list = make_kanji_list()

for finals in finals_dict:

  all_list = []
   
  print("")
  print("**------------ " + finals + " -----------------**  ")

  for spin in finals_dict[finals]:

    out_list = []

    for kanji_info in kanji_list:

      spin_ki = kanji_info[1]

      if spin_ki == spin:

        out_list.append([kanji_info[0]] + kanji_info[2:])

    out_list = remove_duplicates(out_list)

    print("   ","{:10s}".format(spin),out_list, "  ")

    all_list = all_list + out_list

  all_list = remove_duplicates(all_list)
 
  dict = group_by_onyomi_finals(all_list,kks)

  new_dict = sort_with_frequency(dict)

  sum_of_nums = compute_sum(new_dict)

  print("")

  for key in new_dict:

    num = new_dict[key][0]

    percent = 100.0 * num / sum_of_nums

    print(" [ " + key + " ] " + "{:.1f}".format(percent) + "% (" + str(num) + ") " , new_dict[key][1], "  ")
