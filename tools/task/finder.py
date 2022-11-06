
from validate_email import validate_email
from urlextract import URLExtract
from PIL import Image
import pytesseract

from tools.models import EmailExtract, NumberExtract, DomainExtract,Content,Wrodcounter

import random
import re

import PyPDF2
import json



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

    # chardet_type = None
    # try:
    #     # First try the fast C implementation.
    #     #  PyPI package: cchardet
    #     import cchardet
    #     def chardet_dammit(s):
    #         if isinstance(s, str):
    #             return None
    #         return cchardet.detect(s)['encoding']
    # except ImportError:
    #     try:
    #         # Fall back to the pure Python implementation
    #         #  Debian package: python-chardet
    #         #  PyPI package: chardet
    #         import chardet
    #         def chardet_dammit(s):
    #             if isinstance(s, str):
    #                 return None
    #             return chardet.detect(s)['encoding']
    #         #import chardet.constants
    #         #chardet.constants._debug = 1
    #     except ImportError:
    #         # No chardet available.
    #         def chardet_dammit(s):
    #             return None
        # print('text', text)
    return text 

def pdf_to_process(pdf=None):
    file={pdf.name}
    print('file',file)
    # split_file=file.split('')
    # print('split_file',split_file)
    for files in file:
        print('files',files)
        pdf_file = open(files, 'rb')
        print('pdf file',pdf_file)
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        data = json.dumps(page_content)
        print(data)
    # pass
def word_count_process(text=None):
    word_split=len(text.split(' '))
    print('word_split',word_split)
    sentance_split=len(text.split('.'))
    print('sentance_split',sentance_split)
    text_length=len(text)
    print('text_length',text_length)
    
    return text 

def article_process(category=None,article=None):
    articles=[i.article for i in Content.objects.all()] 

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
      
        for article in articles:
            # text=articles.text
            # print('text',article)
            data =article.split(' ')
            datal=len(data)
            newdatalist =data
            
            for i in range(0,datal):
                # if verb in data:
                #     newdatalist[i]=data
                # else:
                # for datas in data:
                    # print('data',datas)  0
                # name=wordnet.synsets(datas)
                list=[]
                for syn in wordnet.synsets(data[i]):
                    # print('data',syn)
                    
                    for l in syn.lemmas():
                        # print('ttttt',type(l))
                        
                        word=l.name()
                        # print('word',word)
                        # break
                        list.append(word)
                        
                

                # print('random',randomss)

                        # # newdatalist[i] =l.name()
                if list:
                    # print('list',list)
                    randomss=random.choice(list)
                    newdatalist[i] =randomss
                # else:
                #     print('empty')
                        # randoms=random.choice(list)
                        # print('randoms',randoms)
                    # synonyms.append(l.name())
                    # if l.antonyms():
                    # antonyms.append(l.antonyms()[0].name())
            # for new in newdatalist:
          
        # print('newdatalist',newdatalist)
        datajoin='-'.join(newdatalist)

        joindata=datajoin.replace("-", " ")
        print('newdatalist',joindata)

        # for chunk in joindata.split('.'):
        # # print('chunk',chunk)
        #     # text =article
        #     settings = TTSettings(do_sample=True, temperature=0.5,  min_length=1, max_length=1000)
        #     articles = happy_tt.generate_text(chunk, args=settings)
        #     article=articles.text
        #     out.append(article)
        # print('article',article)
        # print('syn',set(synonyms))
        # print('atn',set(antonyms))
        # data[tempIndex] = newSyn
        # list = ['a,b,c,d]
        #list[3] = 'z'

    
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