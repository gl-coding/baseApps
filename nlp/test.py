#encoding=utf8
from service_jieba import *

if __name__ == "__main__":
    #test data
    s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
    cuts = jieba.cut(s.strip())

    #test case
    #cixing_dic = load_cixing_ch("./cixing.dic")
    #load_stop_words("./stopword.txt")
    remove_stopwords(cuts)
