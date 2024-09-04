See:
https://research-zy75.hatenadiary.com/entry/2024/08/24/060845

# Files

joyo-variants.txt : 漢字データベースプロジェクトにあった日本の常用漢字と繁体字の対応表。  

onyomi_joyo_school.pdf: 文部科学省のサイトにあった学校で習う常用漢字とその音読みの表。

unihan.rb: 漢字データベースプロジェクトのUnihan Databaseを自分のコンピュータに構築するスクリプト。言語はRuby。 

# 構築

環境: MacOS Ventura

まず、Rubyをインストールし、unihan.rbを使ってUnihan databaseを構築。

以下の４filesは既にrepositoryにある。自分で作る時は、まず削除してから以下を実行。
```
python3 extract_haitohyo_onyomi.py > joyo_onyomi_school.txt

python3 make_pinyin_table_unihan.py > pinyin_table_u.txt

python3 make_kanji_table.py > kanji_table.txt

python3 make_finals_list.py > finals_list.txt

```

# 分析

```
python3 analyze_by_finals.py > by_finals_result.md
```

```
python3 analyze_by_pinyin.py > by_pinyin_result.md

```
