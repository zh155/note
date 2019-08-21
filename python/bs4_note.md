from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title">
<b >The Dormouse's story</b>
<b>The Dormouse's story</b>
<b>The Dormouse's story</b>
</p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# pipenv install lxml      features='xml'
soup = BeautifulSoup(html_doc, features='lxml')
# soup = BeautifulSoup(html_doc)

# 规整打印
# print(soup.prettify())

# 查询title标签
print(soup.title)
# 查询a标签(第一个)
print(soup.a)
# 查询所有a标签
print(soup.find_all('a'))
# 查询a标签里的所有属性 返回字典
print(soup.a.attrs)
# 查询a标签中是否含有class属性  返回True/False
print(soup.a.has_attr('class'))
# 查询p标签中的子标签  ‘\n’ 返回 list_iterator object
print(list(soup.p.children))
# 查询id为link3的标签
print(soup.find(id='link3'))
# 查询id为link3的所有标签
print(soup.find_all(id='link3'))
# 查询所有文字内容 包括 换行符
print(soup.get_text())

# 支持css选择器
# 查询所有 类为story的标签
print(soup.select('.story'))
# 查询所有 id为link1 的标签
print(soup.select('#link1'))
# 查询 story类下的a标签
print(soup.select('.story a'))
# 查询类名为story的p标签
print(soup.select('p.story'))
