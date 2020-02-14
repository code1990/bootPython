# Python XML 解析
# 什么是 XML？
# XML 指可扩展标记语言（eXtensible Markup Language）

# python使用SAX解析xml
# SAX是一种基于事件驱动的 API。
#
# 利用SAX解析XML文档牵涉到两个部分: 解析器和事件处理器。
#
# 解析器负责读取XML文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
#
# 而事件处理器则负责对事件作出响应，对传递的XML数据进行处理。

# ContentHandler类方法介绍
# characters(content)方法
#
# startDocument() 方法
#
# 文档启动的时候调用。
#
# endDocument() 方法
#
# 解析器到达文档结尾时调用。
#
# startElement(name, attrs)方法
#
# 遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。
#
# endElement(name) 方法
#
# 遇到XML结束标签时调用。
#
# make_parser方法
# 以下方法创建一个新的解析器对象并返回。
# parser方法
# 以下方法创建一个 SAX 解析器并解析xml文档：
# parseString方法
# parseString方法创建一个XML解析器并解析xml字符串：

# Python 解析XML实例

import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("movie")
            title = attributes["title"]
            print("title", title)

    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "type":
            print(self.type)
        elif self.CurrentData == "format":
            print(self.format)
        elif self.CurrentData == "year":
            print(self.year)
        elif self.CurrentData == "rating":
            print(self.rating)
        elif self.CurrentData == "stars":
            print(self.stars)
        elif self.CurrentData == "description":
            print(self.description)

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if (__name__ == "__main__"):
    # 创建一个xmlreader
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写contexthandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)
    parser.parse("movie.xml")

#     使用xml.dom解析xml
# 文件对象模型（Document Object Model，简称DOM），是W3C组织推荐的处理可扩展置标语言的标准编程接口。
#
# 一个 DOM 的解析器在解析一个 XML 文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，
#
# python中用xml.dom.minidom来解析xml文件，实例如下：
from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print
    "Root element : %s" % collection.getAttribute("shelf")

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print
    "*****Movie*****"
    if movie.hasAttribute("title"):
        print
        "Title: %s" % movie.getAttribute("title")

    type = movie.getElementsByTagName('type')[0]
    print
    "Type: %s" % type.childNodes[0].data
    format = movie.getElementsByTagName('format')[0]
    print
    "Format: %s" % format.childNodes[0].data
    rating = movie.getElementsByTagName('rating')[0]
    print
    "Rating: %s" % rating.childNodes[0].data
    description = movie.getElementsByTagName('description')[0]
    print
    "Description: %s" % description.childNodes[0].data
