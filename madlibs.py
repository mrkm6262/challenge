import re
text = """キリンは大昔から__複数名詞__の興味の対象でした。キリンは__複数名詞__の中で
一番背が高いですが、科学者たちはそのような長い__体の一部__をどうやって獲得したのか
説明できません。キリンの身長は__数値__ __単位__近くあり、その高さのほとんどは脚と
__体の一部__によるものです。
"""

def mad_libs(mls):
    """
    :palam mls: 文字列で、ユーザーに入力してもらいたい単語(＝ヒント)の部分は後を２つの
    アンダースコアで挟んでください。ヒントの単語にはアンダースコアを含めないでください。
    __hint_hint__はダメです。__hint__はokです。
    """

    hints = re.findall("__.*?__",mls)
    print(hints)
    
    if hints is not None:
        for word in hints:
            q = "{}を入力:".format(word)
            new = input(q)
            mls = mls.replace(word,new,1)
        print('\n')
        mls = mls.replace("\n","")
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)
