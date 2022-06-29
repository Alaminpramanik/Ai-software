from __future__ import absolute_import, unicode_literals                                                                            
from rest_framework.response import Response                                
from rest_framework.exceptions import NotFound
from rest_framework import status

from validate_email import validate_email
from urlextract import URLExtract
from PIL import Image
import pytesseract
from happytransformer import HappyTextToText
from happytransformer import TTSettings
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.corpus import wordnet
import random
import re

from tools.models import EmailExtract, NumberExtract, DomainExtract, ImageToText,AutomaticArticle
happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")

def mail_process(email=None):
   
    emails = set(re.findall(r"[a-zA-Z0-9.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", email))
   
    return emails   

def number_process(phone=None):

    phone = set(re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', phone))
   
    return phone   

def domain_process(link=None):
  
    extractor = URLExtract()
    link = extractor.find_urls(link)
   
    return link 

def image_process(image=None):
    images= Image.open(image)

    images=pytesseract.image_to_string(images,  lang="eng")
    text = images.replace("\r\n", " ").replace("\n", " ").replace("\r", " ").replace('\f', ' ')

    print('text', text)
    return text 
    

def article_process(category=None,article=None):
    articles=[i.article for i in AutomaticArticle.objects.all()] 

    # print('articles',articles)

    match=re.compile (article)
    # print('match',match)
    
    matching=match.search(str(articles))
    # print('matching',matching)
    synonyms = []
    antonyms = []
    out = []
    text=[]
    if matching:
        # for article in articles:
        #     text=article.split('.')
        #     print('article',text)
        #     for texts in text:
        #         settings = TTSettings(do_sample=True, temperature=0.5,  min_length=1, max_length=1000)
        #         artic = happy_tt.generate_text(texts, args=settings)
        #         articl=artic.text
        #         out.append(articl)
        #         print('article',articl)


    # for outs in out:
    #     print('result',outs)
    #     return outs 


    
    # return articl
        for article in articles:
            # text=articles.text
            # print('text',article)
            data =article.split(' ')
            for datas in data:
                # print('data',datas)
                # name=wordnet.synsets(datas)
                for syn in wordnet.synsets(datas):
                    # print('data',syn)
                    for l in syn.lemmas():
                        ran=l.name()
                        print('llll',ran)
                        
                    # synonyms.append(l.name())
                    # if l.antonyms():
                    #     antonyms.append(l.antonyms()[0].name())

        # print('syn',set(synonyms))
        # print('atn',set(antonyms))

    
    #  for datas in data:
    #             print('data',datas)
    #             name=wordnet.synsets(datas)
    #             # print('name',name)
    #             # print(syn[0].name)
    #             # for name in range(1):
    #             print('name',int(name.name()))
    #             # print(name[0].definition())
    #             # print(name[0].examples())
                    # for l in syn.lemmas():
                    #     name=synonyms.append(l.name())
                    #     if l.antonyms():
                    #         antonyms.append(l.antonyms()[0].name())
   
    # return out 


def grammer_process(article=None):


    happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")

    # input='Twitter web services for friends is a '
    # inlen=len(input)

    out = []
    threshold = 50
    for chunk in article.split('.'):
        # print('chunk',chunk)
        text =article
        settings = TTSettings(do_sample=True, temperature=0.5,  min_length=1, max_length=1000)
        articles = happy_tt.generate_text(text, args=settings)
        article=articles.text
        out.append(article)
    print('article',article)
    # print('result',out)

   
    return article 