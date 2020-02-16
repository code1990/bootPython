# Python 使用正则表达式提取字符串中的 URL
import re


def Find(string):
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url


print("Urls: ", Find("https://www.baidu.com"))
