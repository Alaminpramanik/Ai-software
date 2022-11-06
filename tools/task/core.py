import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
nltk.download('universal_tagset')
nltk.download('omw-1.4')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import brown

import random
import re

def keyword_process(keyword=None):
    # print('keyword_process',keyword)
    # for key in keyword:

    keyword_list=set()
    # for keywords in range(10):
    #     print(keywords)
    text= word_tokenize(keyword)
    datal=len(text)
    # print('text',text)
    # print('len',datal)
    newdatalist =text
    sen=nltk.pos_tag(text)
    # print('ssss',sen)
    newdatalist =[]
    for send in sen:
        datal=len(sen)  
        if 'CD' in send or 'CC' in send or 'DT' in send or 'EX' in send or 'FW' in send or 'IN' in send or 'LS' in send or 'MD' in send or 'NNP' in send or 'NNPS' in send or 'PDT' in send or 'POS' in send or 'PRP' in send or 'PRP$' in send or 'RP' in send or 'TO' in send or 'UH' in send or 'VBG' in send or 'VBD' in send or 'VBN' in send or 'VBZ' in send or 'WDT' in send or '.' in send or 'WRB' in send:
            data=send[0]
            newdatalist.append(data)

        if 'NNS' in send or 'NN' in send or 'VB' in send or 'VBP' in send or 'JJ' in send or 'JJR' in send or 'RB' in send or 'RBR' in send or 'RBS' in send or 'JJS' in send:
            list=[]
            data=send[0]
            print('send ',data)
            for syn in wordnet.synsets(data):
                for l in syn.lemmas():
                    word=l.name()
                    list.append(word)           

            if list:
                data=random.choice(list)
                newdatalist.append(data)
                    
    datajoin='-'.join(newdatalist)

    joindata=datajoin.replace("-", " ")
    keyword=joindata.replace("_", " ")
    # keyword_list.add(keyword)
        # print('keyword write',keyword)
    return keyword

def content_process(keyword=None, content=None, str_ref=None):
    print('content_process......',str_ref)
    print('content_process......',content)
    print('keyword....',keyword)
    content_list=[]
    
    # for contents in range(10):
    # print(contents)
    # print('content_process',content_process)
    # for contents in content:
        # print('article',article)

    text= word_tokenize(content)
    datal=len(text)
    # print('text',text)
    # print('len',datal)
    newdatalist =text
    sen=nltk.pos_tag(text)
    print('ssss',sen)
    newdatalist =[]
    
    for send in sen:
        datal=len(sen)
        if 'CD' in send or 'CC' in send or 'NNS' in send or 'NN' in send or 'EX' in send or 'DT' in send  or 'FW' in send or 'IN' in send or 'LS' in send or 'MD' in send or 'NNP' in send or 'NNPS' in send or 'PDT' in send or 'POS' in send or 'PRP' in send or 'PRP$' in send or 'RP' in send or 'TO' in send or 'UH' in send or 'VBG' in send or 'VBD' in send or 'VBN' in send or 'VBP' in send or  'VBZ' in send or 'WDT' in send or '.' in send or 'WRB' in send:
            data=send[0]
            newdatalist.append(data)

        if 'JJ' in send or 'JJR' in send or 'RB' in send or 'VB' in send or 'RBR' in send or 'RBS' in send or 'JJS' in send:
            list=[]
            data=send[0]
            # print('data',data)
            for syn in wordnet.synsets(data):
                for l in syn.lemmas():
                    word=l.name()
                    list.append(word)           

            if list:
                # print('list',list)
                data=random.choice(list)
                newdatalist.append(data)
                    
    datajoin='-'.join(newdatalist)

    joindata=datajoin.replace("-", " ")
    content=joindata.replace("_", " ")
    # content_list.append(content)
    # print('len',len(content_list))
    print('content write',content)
    # return content