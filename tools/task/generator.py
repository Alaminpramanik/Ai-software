from tools.task.core import keyword_process, content_process
from tools.models import Content,ContentKeyword
# happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")

def article_process(keyword=None,content=None):
    keyword_filter = ContentKeyword.objects.filter(keyword=keyword).first()
    # print('keyword_filter',keyword_filter)

    content_filter = Content.objects.filter(content=content).first()
    # print('content_filter',content_filter)
    if keyword_filter is None:
        store_keyword=ContentKeyword.objects.create(keyword=keyword)
        # print('store_keyword',store_keyword)
        store_content=Content.objects.create(keyword=store_keyword,content=content)
        # print('store_content',store_content)
 
    if content_filter is None:
        store_content=Content.objects.create(keyword=store_keyword,content=content)
        print('store_content',store_content)
    
        
    keywords=keyword_process(keyword)
    for keyword in keywords:
        store_keyword=ContentKeyword.objects.create(keyword=keyword)
        print('keyword return',store_keyword)
    contents=content_process(content)
    print('content return',contents)
    store_content=Content.objects.create(keyword=store_keyword,content=contents)
    print('content return',store_content)
  
    return contents