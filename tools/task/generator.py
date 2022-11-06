from os import PRIO_USER
from tools.task.core import keyword_process, content_process
from tools.models import Content,ContentKeyword
# happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")
import requests
from bs4 import BeautifulSoup
import random
from tools.task.scrap import get_data

def article_process(keyword=None, content=None, answer=None, key=None, str_ref=None):
    # print('str_ref......',str_ref)
    # print('answer......',answer)
    # print('key....',key)

    try:
        keyword_filter = ContentKeyword.objects.filter(keyword=keyword).first()
        # print('content_filter',keyword_filter)
        if keyword_filter is None:
            store_keyword=ContentKeyword.objects.create(keyword=keyword)
            if store_keyword:
            # print('store_keyword',store_keyword)
                store_content=Content.objects.create(keyword=store_keyword,content=content)
            # print('store_content',store_content)

        if keyword_filter:
            content_filter = Content.objects.filter(content=content).first()
            if content_filter is None:
                store_content=Content.objects.create(keyword=keyword_filter,content=content)
    except Exception as e:
        print('error some keyword or content')

    
    try:
        keyword_filter = ContentKeyword.objects.filter(keyword=key).first()
        # print('content_filter',keyword_filter)
        if keyword_filter is None:
            store_keyword=ContentKeyword.objects.create(keyword=key)
            if store_keyword:
            # print('store_keyword',store_keyword)
                store_content=Content.objects.create(keyword=store_keyword,content=answer)
            # print('store_content',store_content)

        if keyword_filter:
            content_filter = Content.objects.filter(content=answer).first()
            if content_filter is None:
                store_content=Content.objects.create(keyword=keyword_filter,content=answer)

    except Exception as e:
        print('error some keyword or content')
    
    contents=content_process(keyword=key,content=answer,str_ref=str_ref)
    # print('content return',contents)
    # store_content=Content.objects.create(keyword=store_keywords,content=contents)
    # print('content return',store_content)

   
    # return contents

def content_write(keyword=None,category=None,str_ref=None):
    try:
        if category:
            print('category',category)
            content=get_data(keyword)
            key=keyword
            str_ref=str_ref

            link=set(content.find_all('div', attrs={'class':'compTitle options-toggle'}))
            for anchor in link:
                # print(anchor)
                urls=anchor.find_all('a', href=True)

                for url in urls:
                    print('url',url['href'])
            #     content=get_data(url)
 
                

    except Exception as e:
        print('eroor')

    try:
        content=get_data(keyword)
        # print('str_ref...........',str_ref)
        # print(keyword)
        # print('keyword',keyword)
        key=keyword
        str_ref=str_ref
        # print('keyword',key)
        # 

        compText=set(content.find_all('span', attrs={'class':'fc-falcon'}))
        # print('compText',compText)
        compTextList=set(content.find_all('span', attrs={'class':'cur-p c-black fz-15 lh-17 va-top'}))
        # print('compText',compText)
        compContainerExp=content.find_all('div', attrs={'class':'cnt mt-0'})


        for teee in compContainerExp:
            title=teee.find_all('div', attrs={'class':'compText'})
            # keyword=title.text
            # print('questions list',title)
            paragraph=teee.find_all('div', attrs={'class':'compTextList'})
            # keyword=paragraph.text
            # print('ppppp list',paragraph)
            for titles in title:
                for paragraphs in paragraph:
                    question=titles.text
                    # print('question',question)
                    passage=paragraphs.text
                    # print('passage -------',passage)
                    keyword=article_process(keyword=question,content=passage)
            
        for teee in compText:
            question=teee.text
            keyword=article_process(keyword=key,content=question)
        
        content=set(content.find_all('li', attrs={'class':'va-top ov-h'}))
        for cont in content:
            content=cont.text
            keyword=article_process(key=key,answer=content, str_ref=str_ref)
    except Exception as e:
        print('eroor')


    # return keyword