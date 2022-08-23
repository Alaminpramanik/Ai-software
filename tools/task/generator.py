from os import PRIO_USER
from tools.task.core import keyword_process, content_process
from tools.models import Content,ContentKeyword
# happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")
import requests
from bs4 import BeautifulSoup
import random
from tools.task.scrap import get_data

def article_process(keyword=None,content=None):
    keyword_filter = ContentKeyword.objects.filter(keyword=keyword).first()
    # print('keyword_filter',keyword_filter)

    try:
        # print('content_filter',content_filter)
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
            # print('store_content',store_content)
    except Exception as e:
        print('error some keyword or content')
    
        
    keywords=keyword_process(keyword)
    # for keyword in keywords:
    store_keywords=ContentKeyword.objects.create(keyword=keyword)
        # print('keyword return',store_keyword)
    contents=content_process(content)
    # print('content return',contents)
    store_content=Content.objects.create(keyword=store_keywords,content=contents)
    # print('content return',store_content)

   
    return contents

def content_write(keyword=None,category=None,str_ref=None):
    content=get_data(keyword)
    # print(keyword)
   
    print('textsc contents',content)
    link=content.find_all({"a"})
    # for links in link:
    #     print('body link',links.text)
    # links=set(content.find_all('a', attrs={'class':'ls-05'})) ##aol
    for anchor in link:
        url = anchor.attrs["href"] if "href" in anchor.attrs else ''
        content=get_data(url)

        # print('textsc contents',content)

    # textsc=set(content.find_all('p', attrs={'class':'lh-16'})) ##aol  
    # # rndom_choice=textsc.text
    # textsc=set(content.find_all('div', attrs={'class':'compImageProfile'}))
    # # textsc=set(content.find_all('div', attrs={'class':'compContainerUL'}))

    # # textsc=set(content.find_all('div', attrs={'class':'compText'}))

    # # textsc=set(content.find_all('div', attrs={'class':'compContainerExp'}))

    # # print('textsc',textsc)
    # # textsc=content.find_all({"class": 'compContainerUL'})
    # # print('textsc rndom_choice',rndom_choice)
    
    # list=[]
    # for teee in textsc:
    #     list.append(teee)
    #     # return keyword
    #     # keyword=teee.text
    #     # print('list content',list)
    #     # content_text=teee.text
    #     # keyword=article_process(keyword=keyword,content=content_text)

    # if list:
    #     data=random.choice(list)
    #     # print('data',data)
    #     keyword=data.text
    #     # print('content_text',content_text)
    #     # keyword=article_process(keyword=keyword,content=content_text)


    # return keyword