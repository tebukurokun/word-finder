from typing import List

import MeCab
import unidic

# ひらがなリスト
hiragana_list = list(
    "あいうえお"
    "かきくけこがぎぐげご"
    "さしすせそざじずぜぞ"
    "たちつてとだぢづでど"
    "なにぬねの"
    "はひふへほばびぶべぼぱぴぷぺぽ"
    "まみむめも"
    "やゆよ"
    "らりるれろ"
    "わをん"
    "っ"
    "アイウエオ"
    "カキクケコガギグゲゴ"
    "サシスセソザジズゼゾ"
    "タチツテトダヂヅデド"
    "ナニヌネノ"
    "ハヒフヘホバビブベボパピプペポ"
    "マミムメモ"
    "ヤユヨ"
    "ラリルレロ"
    "ワヲン"
    "ッ"
    "ー"
)

# 辞書のpathは環境に応じて変えてね
dict_dirs = [
    f"-d {unidic.DICDIR}",
    f"-d /opt/homebrew/lib/mecab/dic/ipadic",
    f"-d /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd",
]


def main():
    """
    main
    :return:
    """

    # 1文字目、3文字目、4文字目は同じ、2文字目が異なる組み合わせを作成
    combinations = [
        f"{char}{second_char}{char}{char}"
        for char in hiragana_list
        for second_char in hiragana_list
        if char != second_char
    ]

    print({"combinations": combinations})

    valid_words = set()

    # 各辞書ファイルに対して find_valid_words を実行
    for dict_dir in dict_dirs:
        valid_words.update(find_valid_words(dict_dir, combinations))

    # 辞書に存在する4文字の単語を表示
    print({"valid_words": valid_words})


def find_valid_words(dict_dir: str, words: List[str]) -> List[str]:
    """
    単語リストから存在する単語を抽出.
    :param dict_dir: mecabで使う辞書ファイル
    :param words: チェックしたい単語リスト
    :return: 存在した単語リスト
    """

    mecab = MeCab.Tagger(dict_dir)

    # 存在する単語を格納するリスト
    valid_words = [word for word in words if is_valid_word(mecab, word)]

    return valid_words


def is_valid_word(mecab: MeCab.Tagger, word: str) -> bool:
    """
    辞書に存在する単語か判定.
    :param mecab: MeCab.Tagger
    :param word: 単語.
    :return:
    """

    # MeCabで解析して、解析結果が単語と一致するかチェック
    node = mecab.parseToNode(word)

    # 最初のノードが入力単語と一致するか確認
    while node:
        features = node.feature.split(",")

        if all(f == "*" for f in features[3:]):
            # 無効なノード (名詞,一般,*,*,*,*,* のような形式) をスキップ
            node = node.next
            continue

        if node.surface == word and (
            "名詞" in node.feature or "副詞" in node.feature
        ):  # 名詞 or 副詞が含まれているかをチェック
            print(node.feature)
            return True  # 辞書に存在する単語
        node = node.next  # 次のノードに移動

    return False


if __name__ == "__main__":
    main()
