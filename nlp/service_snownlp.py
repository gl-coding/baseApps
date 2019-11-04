#encoding=utf-8
from snownlp import SnowNLP
import jieba_serve as js
import re
import os

# SnowNLP库：
# words：分词
# tags：关键词
# sentiments：情感度
# pinyin：拼音
# keywords(limit)：关键词
# summary：关键句子
# sentences：句子
# tf：tf值
# idf：idf值

def load_stop_words(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

def seg_sentence(sentence_seged):
    #sentence_seged = jieba.cut(sentence.strip())
    stopwords = load_stop_words('stopwords.txt')  # 这里加载停用词的路径
    outstr = []
    for word in sentence_seged:
        if word not in stopwords:
            outstr.append(word)
    return outstr

def is_han(string):
    string = string.decode("utf-8")
    pat = re.compile(ur'[\u4e00-\u9fa5]+')
    res = ""
    for item in pat.findall(string):
        #print item
        res += item
    return res.strip().encode("utf-8")

def cp_file(filename):
    command = 'head -n 3000 "' + filename + '" | iconv -f gb18030 -t utf-8 > ./test.txt'
    os.system(command)

def merge_article_lines(filename):
    res = ""
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
            line = line.strip().replace("\xe3\x80\x80", "")
            if len(line) < 100 or len(line) > 120:
                continue
            #if count%2 == 0:
            res += line + "\n"
    print count
    return res

def get_article_summary(filename):
    res = merge_article_lines(filename)
    s = SnowNLP(res)
    for su in s.summary(1):
        print su

def get_article_summary_res(res):
    summary_res = set()
    s = SnowNLP(res)
    for su in s.summary(8):
        #print "summary:"
        summary_res.add(su.strip().replace("\xe3\x80\x80", ""))
    #for item in summary_res:
    #    print item
    return summary_res

#get_article_summary("./data.article")

def get_article_keyword(filename):
    res = merge_article_lines(filename)
    print js.get_key_word(res, 5)

def get_article_keyword_str(res, count):
    #print "keyword:"
    res = js.get_key_word(res, count).encode("utf-8")
    #print res
    return res

def get_article_keyword_list(res, count):
    print "keyword:"
    res_list = []
    res = js.get_key_word(res, count).encode("utf-8")
    for item in res.split(","):
        res_list.append({"name":"关键词："+item, "children":[]})
    return res_list

def get_article_keyword_freq(res):
    #print res
    res_list = js.get_topn(res, 200)
    #print res_list
    key = []
    val = []
    for item in res_list:
        key.append(item[0])
        val.append(item[1])
    return (key, val)

#get_article_keyword("./data.article")

def get_info(filename):
    cp_file(filename)
    res = merge_article_lines("./test.txt")
    summ = get_article_summary_res(res)
    keywords = get_article_keyword_str(res, 10)
    treenodes = get_article_keyword_list(res, 5)
    freq = get_article_keyword_freq(res)
    return summ, keywords, treenodes, freq

filename = "snownlp_serve.py"
#get_info(filename)

