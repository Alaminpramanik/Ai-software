import requests
from bs4 import BeautifulSoup

def get_data(keyword=None,url=None):
    if keyword:
        url='https://search.yahoo.com/search;_ylt=Awr.1ZuWtP9i8EwDWtxDDWVH;_ylc=X1MDMTE5NzgwNDg2NwRfcgMyBGZyAwRmcjIDcDpzLHY6c2ZwLG06c2EtZ3Atc2VhcmNoBGdwcmlkA1o3QlRfR25xUjZTbWR5TFRiYV90VUEEbl9yc2x0AzAEbl9zdWdnAzEEb3JpZ2luA3NlYXJjaC55YWhvby5jb20EcG9zAzEEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzI3BHF1ZXJ5A2hvdyUyMHRvJTIwbWFrZSUyMG1vbmV5JTIwaW4lMjBvbmxpbmUEdF9zdG1wAzE2NjA5MjUwODEEdXNlX2Nhc2UD?p='+keyword
    else:
        url=url
    text = ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    
    # print('url',url)
    try:
        res = requests.get(url, headers=headers, timeout=30)
        text += res.text
    except Exception as e:
        print('Connection Aborted! contact', e)
    
    # print('text ', text)
    content = BeautifulSoup(text, 'html.parser')
    return content