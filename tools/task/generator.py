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

from tools.models import Content,ContentKeyword
# happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")

def article_process(keyword=None,content=None):
    store_keyword=ContentKeyword.objects.create(keyword=keyword)
    print('store_keyword',store_keyword)

    # keyword_id=ContentKeyword.objects.get(id=keyword)
    # print('id',keyword_id)

    store_content=Content.objects.create(keyword=store_keyword,content=content)
    print('store_content',store_content)
    # contents=[i.content for i in Content.objects.all()] 

    # # print('articles',articles)

    # match=re.compile (content)
    # # print('match',match)
    
    # matching=match.search(str(content))
    # # print('matching',matching)
    # synonyms = []
    # antonyms = []
    # out = []
    # text=[]

    # if matching:
    #     # print('matching',matching)
    #     for article in contents:
    #         # print('article',article)

    #         text= word_tokenize(article)
    #         datal=len(text)
    #         # print('text',text)
    #         # print('len',datal)
    #         newdatalist =text
    #         sen=nltk.pos_tag(text)
    #         print('ssss',sen)
    #         newdatalist =[]
    #         for send in sen:
    #             datal=len(sen)
    #             if 'CD' in send or 'CC' in send or 'DT' in send or 'EX' in send or 'FW' in send or 'IN' in send or 'LS' in send or 'MD' in send or 'NN' in send or 'NNP' in send or 'NNPS' in send or 'PDT' in send or 'POS' in send or 'PRP' in send or 'PRP$' in send or 'RP' in send or 'TO' in send or 'UH' in send or 'VBG' in send or 'VBD' in send or 'VBN' in send or 'VBZ' in send or 'WDT' in send or '.' in send or 'WRB' in send or 'VB' in send:
    #                 data=send[0]
    #                 newdatalist.append(data)

    #             if 'NNS' in send or 'VBP' in send or 'JJ' in send or 'JJR' in send or 'RB' in send or 'RBR' in send or 'RBS' in send or 'JJS' in send:
    #                 list=[]
    #                 data=send[0]
    #                 for syn in wordnet.synsets(data):
    #                     for l in syn.lemmas():
    #                         word=l.name()
    #                         list.append(word)           

    #                 if list:
    #                     data=random.choice(list)
    #                     newdatalist.append(data)
                            
    #         datajoin='-'.join(newdatalist)

    #         joindata=datajoin.replace("-", " ")
    #         joindatas=joindata.replace("_", " ")
    #         print('joindatas',joindatas)
    # return joindatas