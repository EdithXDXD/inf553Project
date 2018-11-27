import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

import json
def parseJsonFile(filename):
    features = {"food":0, "pizza":0, "flavor":0, "service":1, "friendly":1, "parking":2,\
    "noise":3, "noisy":3, "crowded":4, "crowd":4, "price":5, "priced":5, "money":5, "cheap":5, \
    "expensive":5, "environment":6}
    
    sid = SentimentIntensityAnalyzer()
    data = []
    line_cnt=0

    outfile = open("vector_"+filename, "w")
    with open(filename) as file:
        for line in file:
            oneline = json.loads(line)
            data.append(oneline)
            user_id = oneline["user_id"]
            business_id = oneline["business_id"]
            review_text = oneline["text"].lower()
            #lines_list = tokenize.sent_tokenize(review_text)
            #for x in lines_list:

            words = nltk.word_tokenize(review_text)
            words_len=len(words)
            word_set = set(words)
            
            one_vector = [0, 0, 0, 0, 0, 0, 0]
            for each_feature in features:
                if each_feature in word_set:
                    idx = words.index(each_feature)
                    st = 0
                    if idx>5:
                        st = idx-5
                    ed = words_len-1
                    if idx+5<words_len:
                        ed = idx+5
                    sub_text=""
                    for i in range(st, ed+1):
                        sub_text += (words[i]+" ")
                    ss = sid.polarity_scores(sub_text)
                    if ss["pos"]>ss["neg"]:
                        one_vector[features[each_feature]]+=ss["pos"]
                    else:
                        one_vector[features[each_feature]]-=ss["neg"]  
            out_str = user_id+" "+business_id
            for i in range(7):
                out_str+= (" "+str(one_vector[i]))

            print >> outfile, out_str

            if line_cnt<10:
                print(out_str)
            line_cnt+=1

    outfile.close()
    print "line_cnt:", line_cnt

parseJsonFile("review_part1.txt")
"""
sentence = "what a good day! I think it's great, and what do you think? Maybe you will like it; I hope"
lines_list = tokenize.sent_tokenize(sentence)
print lines_list
sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores("today and the food is delicious")
print(ss)
"""