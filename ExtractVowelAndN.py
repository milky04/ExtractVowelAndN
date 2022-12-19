# pykakasiをimport
import pykakasi
kakasi = pykakasi.kakasi()

# textの先頭の'々'を削除したうえで、textの'々'を1文字前の文字に置換する関数
def replace_kurikaesi(text):
  # textの先頭に'々'がある場合、0文字目～'々'が出現しなくなるまで'々'を削除
  text = text.lstrip('々')
  # textをリストに変換
  text_list = list(text)
  # 文字数カウント
  word_cnt = 0
  # text_listから文字を1文字ずつ取り出して'々'かどうかを判別
  for word in text_list:
    # wordが'々'だった場合、wordの'々'を1文字前の文字に置換
    if word == '々':
      text_list[word_cnt] = text_list[word_cnt-1]
    word_cnt += 1
  # text_listをリストから文字列に戻す
  replaced_kurikaesi_text = "".join(text_list)
  # textの'々'を1文字前の文字に置換したtextを返す
  return replaced_kurikaesi_text

# textをword_typeで指定した種類(ひらがな、ローマ字等)の文字列に変換して、空欄で単語ごとに区別した状態で連結したtextを返す関数
def convert_word_type_text(text, word_type):
  # 文章をkakasiに突っ込んで、単語ごとに分解されたリストを取得(単語は辞書型で色々な形式に変換された状態で格納されている)
  word_list = kakasi.convert(text)
  # word_listからword_typeで指定された種類(ひらがな、ローマ字等)の文字列のみを抽出
  word_list_len = len(word_list)
  word_type_word_list = [word_list[cnt][word_type] for cnt in range(word_list_len)]
  # 単語間に空欄を追加して単語ごとに区別した状態で単語を連結する
  word_type_text = " ".join(word_type_word_list)
  # word_typeで指定した種類の文字列に変換して、空欄で単語ごとに区別した状態で連結したtextを返す
  return word_type_text

# ひらがなのtextの'にゃ','にゅ','にょ'をそれぞれの母音('あ','う','お')に変換する関数
def convert_nyanyunyo_to_vowel(text):
  # 'にゃ','にゅ','にょ'にそれぞれ対応する母音('あ','う','お')の辞書
  nyanyunyo_vowel_dict =  {'にゃ':'あ', 'にゅ':'う', 'にょ':'お'}
  # 'にゃ','にゅ','にょ'をそれぞれ対応する母音に変換
  for key, value in nyanyunyo_vowel_dict.items():
    text = text.replace(key, value)
  # 'にゃ','にゅ','にょ'をそれぞれの母音に変換したtextを返す
  return text

# ローマ字のtextから母音と"ん"をひらがなに変換したうえで抽出する関数
def extract_vowel_and_n(text):
  # ローマ字に対応するひらがなの母音と"ん"の辞書
  hiragana_vowel_and_n_dict = {'a':'あ','i':'い','u':'う','e':'え','o':'お','n':'ん'}
  # hiragana_vowel_and_n_dictのコピーを作成
  hiragana_vowel_dict = hiragana_vowel_and_n_dict.copy()
  # hiragana_vowel_dictから"ん"を削除して母音のみの辞書を作成
  hiragana_vowel_dict.pop('n')
  # 出力用の空のvowel_and_n_textを作成
  vowel_and_n_text = ""
  # 文字数カウント
  word_cnt = 0
  # ローマ字のtextからローマ字の母音と"ん"を取り出し
  for word in text:
    word_cnt += 1
    # wordがローマ字の母音なら対応するひらがなの母音をvowel_and_n_textに加える。
    # または'n'かつ最後の文字or'n'の後ろに"'"が付いているor'n'の後ろの文字が母音ではないなら「ん」確定なのでvowel_and_n_textに加える(それ以外はな行の文字なのでpass)。
    if (word in hiragana_vowel_dict) or ((word == 'n') and ((len(text) == word_cnt) or (text[word_cnt] == "'") or (text[word_cnt] not in hiragana_vowel_dict))):
      vowel_and_n_text += hiragana_vowel_and_n_dict[word]
    # 母音と"ん"以外ならpass
    else:
      pass
  # 母音と"ん"を抽出したtextを返す
  return vowel_and_n_text

# 例文
text = '々々々あ々々々諸々々々徐々々々なにぬねのにゃにゅんにょん'
# textの先頭の'々'を削除したうえで、textの'々'を1文字前の文字に置換
replaced_kurikaesi_text = replace_kurikaesi(text)
# replaced_kurikaesi_textをひらがな('hira')に変換して、空欄で単語ごとに区別した状態で連結
hira_text = convert_word_type_text(replaced_kurikaesi_text, 'hira')
# hira_textの'にゃ','にゅ','にょ'をそれぞれの母音('あ','う','お')に変換
hira_text = convert_nyanyunyo_to_vowel(hira_text)
# hira_textをローマ字('kunrei'(訓令))に変換して、空欄で単語ごとに区別した状態で連結
kunrei_text = convert_word_type_text(hira_text, 'kunrei')
# kunrei_textから母音と"ん"をひらがなに変換したうえで抽出
vowel_and_n_text = extract_vowel_and_n(kunrei_text)
# 母音と"ん"を抽出した文字列を出力
print(vowel_and_n_text)
