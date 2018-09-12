# -*- coding:utf-8 -*-

# Created on 2018/9/12
# twitter text 针对LDA模型来作预处理


import nltk
import re

#read in stopwords list:
with open('topic modelling/models/stopwords.txt', 'r') as f:
    stopwords = [word.strip() for word in f.readlines()]

#找一些常见的符号文本
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '#', '$', '%', '...']
expressions = [':-)', ':)', '=)', ':D', ':-(', ':(', '=(', ';(']
#做一个set包含了停用词及各种标点符号
remove_words = set(english_stopwords + english_punctuations + expressions)
#借助nltk作词形还原
wnl = nltk.WordNetLemmatizer()



def filter_tweet(t):
	'''
	对单条tweet进行预处理
	'''
	#全部小写处理
	t = t.lower()
	# 替换tweet Url and user mentions
    t = re.sub(r"(http[s:…]*(//\S*)?)|(@\w+)", "", t)
    #分词+词性还原
    t = [wnl.lemmatize(word) for word in nltk.word_tokenize(t)]
    #去除停用词，过滤超短词
    t = [word for word in t if word not in remove_words and len(word) >= 2]
    return t


def filter_tweets(original_tweets):
	'''
	批量处理tweet，借助单个处理的function
	'''

    _filter_tweets = list(map(filter_tweet, original_tweets))
    res_tweets = []
    res_tweets_filter = []
    for i, f_tweet in enumerate(_filter_tweets):
        if f_tweet:
            res_tweets.append(original_tweets[i])
            res_tweets_filter.append(f_tweet)
    return res_tweets, res_tweets_filter





#测试一下：没问题
def main():
    txt = "RT @SocialWebMining rta Mining women https://hrwhdsd.me 1M+ Tweets @hrwhisper About #Syria http://wp.me/p3QiJd-1I https:…"
    print (filter_tweet(txt))
    txt = "RT @StewySongs: People are people, families are families &amp; lives are lives the world over. The UK is shoulder to shoulder with Paris https:…"
    print (filter_tweet(txt))

    for i, word in enumerate(english_stopwords):
        if word not in stopwords:
            print (word)

    print (wnl.lemmatize('followed'), wnl.lemmatize('following'))


if __name__ == '__main__':
    main()









