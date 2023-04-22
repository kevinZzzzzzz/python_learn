# 解决抓取内容出现ssl错误问题
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import json
import jsonpath

obj = json.load(open('data.json', 'r', encoding='utf-8'))
# print(obj)
# 书店所有书的作者
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(author_list)

# 所有的作者
author_list1 = jsonpath.jsonpath(obj, '$..author')
print(author_list1)

# store下面所有的内容
tag_list = jsonpath.jsonpath(obj, '$.store.*')
print(tag_list)

# store下面所有的price
price_list = jsonpath.jsonpath(obj, '$.store..price')
print(price_list)

# 第三本书
book3 = jsonpath.jsonpath(obj, '$..book[2]')
print(book3)

# 最后一本书
bookLast = jsonpath.jsonpath(obj, '$..book[(@.length - 1)]')
print(bookLast)

# 前两本书
# book_1_2 = jsonpath.jsonpath(obj, '$..book[0,1]')
book_1_2 = jsonpath.jsonpath(obj, '$..book[:2]')
print(book_1_2)

# 过滤出所有包含isbn的书
# 条件过滤需要在()前面添加一个？
book_has_isbn = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(book_has_isbn)

# 价格超过3元
book_price_pass3 = jsonpath.jsonpath(obj, '$..book[?(@.price>3)]')
print(book_price_pass3)

