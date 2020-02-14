# Python3 JSON 数据解析
# JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。
#
# Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
#
# json.dumps(): 对数据进行编码。
# json.loads(): 对数据进行解码。

# json.dumps 与 json.loads 实例
import  json
data = {
    "1":1,
    "name":"test",
    "url":"www.baidu.com"
}
json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

# 处理json文件是由下面的形式
with open("data.json","w") as f:
    json.dump(data,f)

# 读取数据
with open("data.json","r") as f:
    data=json.load(f)