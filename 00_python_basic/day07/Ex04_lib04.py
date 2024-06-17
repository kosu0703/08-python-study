# urllib : url 을 읽고 분석할 때 사용하는 모듈

import urllib.request 

def getWikiDocs(page) :
    resource = 'https://wikidocs.net/{}' .format(page)
    
    with urllib.request.urlopen(resource) as s :
        with open('day07/wikidocs_%s.html' % page, "wb") as f :
            f.write(s.read())

getWikiDocs(12)

import webbrowser

# open_new : 새창에 브라우저 열기
# open : 기존 창에 열기
webbrowser.open_new("http://python.org")






