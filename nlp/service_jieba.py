#encoding=utf-8
import jieba
import jieba.posseg as psg
import jieba.analyse 
import json
import re
from   utils  import *

def load_cixing_ch(filename):
    res_dic = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            idx = line.index(" ")
            key = line[:idx]
            val = line[idx:]
            res_dic[key] = val
            #print key, val
    return res_dic

@deco
def load_stop_words(filepath):
    stopwords = [line.strip().decode("utf-8") for line in open(filepath, 'r').readlines()]
    return stopwords

def remove_stopwords(sentence_seged):
    #sentence_seged = jieba.cut(sentence.strip())
    stopwords = load_stop_words('stopword.txt')  # 这里加载停用词的路径
    outstr = []
    for word in sentence_seged:
        if word not in stopwords:
            outstr.append(word)
    return outstr

s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
sentence_seged = jieba.cut(s.strip())
print sentence_seged
exit()
res = remove_stopwords(sentence_seged)
print ",".join(res)
exit()

def extract_han(string):
    patten = re.compile(ur'[\u4e00-\u9fa5]+')
    res = ""
    for item in patten.findall(string):
        res += item
    return res.strip().encode("utf-8")

#print extract_han(u"x郭磊")
#exit()

def get_normal_fenci(s):
    cut = jieba.cut(s)
    return ','.join(cut)

#s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
#print get_normal_fenci(s)
#exit()

def get_notfull_fenci(s):
    cut = jieba.cut(s,cut_all = False)
    return ','.join(cut)

#s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
#print get_notfull_fenci(s)
#exit()

def get_full_fenci(s):
    cut = jieba.cut(s,cut_all = True)
    return ','.join(cut)

#s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
#print get_full_fenci(s)
#exit()

def get_search_fenci(s):
    cut = jieba.cut_for_search(s)
    return ','.join(cut)

#s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
#print get_search_fenci(s)
#exit()

def get_cut_word_cixing(arg, parallel=False, num=1):
    if not parallel:
        s = arg
        res = psg.cut(s)
        return {x.word:x.flag for x in res}
    else:
        filename = arg
        s = open(filename).read()
        jieba.enable_parallel(parallel)
        res = psg.cut(s)
        jieba.disable_parallel()
        return {x.word:x.flag for x in res}

def print_word_cixing(word_dic):
    for k, v in word_dic.items():
        #print k, cixing_dic.get(v, "")
        print k, v

#s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
#res = get_cut_word_cixing(s)
#print_word_cixing(res)
#exit()

def get_topK_keyword(s, n):
    tags = jieba.analyse.extract_tags(s, topK = n)
    return ",".join(tags)

#s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
#print get_topK_keyword(s, 2)
#print get_topK_keyword(s, 3)
#print get_topK_keyword(s, 4)
#exit()

def get_file_cut_word_parallel(filename, parallel=2):
    file_text = open(filename).read()
    jieba.enable_parallel(parallel)
    file_words = [x for x in jieba.cut(file_text) if len(x) >= 2]
    jieba.disable_parallel()
    return file_words

#res = get_word_parallel("./article.txt", parallel=2)
#print ",".join(res)
#exit()

def get_topN_count_word(content, count):
    from collections import Counter
    words = get_search_fenci(content)
    c = Counter(words).most_common(count)
    return c

#s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
#print get_topN_count_word(s, 3)
#exit()

def get_cut_word_after_userdic(user_dic, s):
    jieba.load_userdict(user_dic)
    res = jieba.cut(s)
    return ','.join(res)

#s = u"我想知道区块链是什么"
#print get_cut_word_after_userdic("./user_dic.txt", s)
#exit()
