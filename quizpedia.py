"""

"""
import requests
import time
import re

CONST_MAX_QUESTION_LINES = 5

def get_wikipedia_article():
    #wikipediaに接続するための基本設定
    S = requests.Session()
    URL = "https://ja.wikipedia.org/w/api.php"

    #wikipedia記事のidとタイトルをランダムに1件取得するためのパラメータの設定
    RANDOM_PARAMS = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": "1",
        "rnnamespace": "0"
    }

    #記事本体を取得するためのパラメータの設定
    ARTICLE_PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,
        "exsectionformat": "plain",
    }

    #ランダムな記事のIDとタイトルを取得
    RANDOM_R = S.get(url=URL, params=RANDOM_PARAMS)
    RANDOM_DATA = RANDOM_R.json()
    page_id = RANDOM_DATA["query"]["random"][0]["id"]
    title = RANDOM_DATA["query"]["random"][0]["title"]

    #ページIDから記事情報の取得
    ARTICLE_PARAMS["pageids"] = str(page_id)
    ARTICLE_R = S.get(url=URL, params=ARTICLE_PARAMS)
    ARTICLE_DATA = ARTICLE_R.json()
    #結果の出力
    return title,ARTICLE_DATA["query"]["pages"][str(page_id)]["extract"]

def get_list_sentence():
    title, article = get_wikipedia_article()
    list_sentence = re.split("。", article.replace("\n",""))

    return title, list_sentence


def make_quiz(title, list_sentence):
    dict_quiz = {}
    dict_quiz["answer"] = title

    dict_quiz["question_1"] = re.sub(title+"|\（.+?\）", "???", list_sentence[0])
    for i in range(1,CONST_MAX_QUESTION_LINES):
        if i < len(list_sentence):
            dict_quiz["question_"+str(i+1)] = re.sub(title, "???", list_sentence[i])

    return dict_quiz




def main():
    print("test")
    title, list_sentence = get_list_sentence()
    dict_quiz = make_quiz(title, list_sentence)

    print(dict_quiz)


if __name__=="__main__":
    main()