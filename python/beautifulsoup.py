# -*- coding: utf-8 -*-
"""BeautifulSoup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ronIhArXJNed1Bfb7PrQHfMUavmAy-T
"""

!pip install bs4

import bs4
import requests

url = 'https://search.shopping.naver.com/search/category/100005307'
result = requests.get(url).text #해당 사이트 url 불러오기

result

bsObj = bs4.BeautifulSoup(result, 'html.parser') #데이터를 처리하기 좋게 파싱함

bsObj.find('a',{'class':'basicList_link__JLQJf'}).text #a태그인 링크를 찾고 그 중 해당 클래스의 택스트를 찾아라

items = bsObj.find_all('a',{'class':'basicList_link__JLQJf'})

for item in items: #아이템 갯수만큼 반복
  print(item.text)

print(items[0].text)
print(items[1].text)
print(items[2].text)
print(items[3].text)

