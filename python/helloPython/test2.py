import re

str = 'https://blog.csdn.net/dreajay/article/details/18001195'
# print(re.match(r'((https?|ftp|file):\/\/)?[-A-Za-z0-9+&@#\/%?=~_|!:,.;]+\.[-A-Za-z+]+\/+/g', str))
print(re.search(r'((https?|ftp|file):\/\/)?[-A-Za-z0-9+&@#\/%?=~_|!:,.;]+\.[-A-Za-z+]+\/+/g',str ))
# print(re.match(r'[0-9a-zA-Z_]{0,19}@163.com',"13@163.com"))
# regular = re.compile(r'/((https?|ftp|file):\/\/)?[-A-Za-z0-9+&@#\/%?=~_|!:,.;]+\.[-A-Za-z+]+\/+/g')
# print(re.findall(regular, str))
# link = 'http://www.discuz.net/thread-3778501-23-1.html'
#
# link_regex=r'thread-(/d+)-(/d+)-1.html'
# print(re.search(link_regex, link))
url_dict_2={}
print(url_dict_2.get("1"))