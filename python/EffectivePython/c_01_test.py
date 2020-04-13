import unittest
import sys
class c_01_test(unittest.TestCase):
	def test_1(self):
		#第1条：确认自己所用的Python版本
		# python --version
		# python3 --version
		print(sys.version_info)
		print(sys.version)
		print("")

	def test_2(self):
		#第2条：遵循PEP8风格指南
		# 8号Python增强提案）又叫PEP 8，
		# 使用space（空格）来表示缩进，而不要用tab（制表符）。
		# 和语法相关的每一层缩进 都用4个空格来表示。
		# 每行的字符数不应超过79。
		# 文件中的函数与类之间应该用两个空行隔开。
		# 类中各方法之间应该用一个空行隔开。
		#
		# 函数、变量及属性应该用小写字母来拼写，各单词之间以下划线相连，例如lowercase_underscore。
		# 受保护的实例属性，应该以单个下划线开头，例如，_leading._underscore。
		# 私有的实例属性，应该以两个下划线开头，例如，_double_leading._underscore。
		# 类与异常，应该以每个单词首字母均大写的形式来命名，例如，CapitalizedWord。
		# 模块级别的常量，应该全部采用大写字母来拼写，各单词之间以下划线相连，例如，ALL CAPS。
		#
		# 类中的实例方法（instance method），应该把首个参数命名为self，以表示该对象自身。
		# 类方法（class method）的首个参数，应该命名为cls，以表示该类自身。
		# 写if a is not b而不是if notaisb。
		# 采用if not somelist这种写法来判断，它会假定：空值将自动评估为False。
		# if somelist语句默认会把非空的值判断为True。
		# 不要编写单行的if语句、for 循环、while 循环及except复合语句
		# import语句应该总是放在文件开头。
		# 引人模块的时候，总是应该使用绝对名称
		# 如果一定要以相对名称来编写import语句，那就采用明确的写法：from.import foo，
		# 文件中的那些import语句应该按顺序划分成三个部分，分别表示标准库模块、
		# 第三方模块以及自用模块。在每一部分之中，各import语句应该按模块的字母顺序来排列。
		# Pylint（htp://ww.ylit.or/）是一款流行的Python源码静态分析工具。
		print("")

	def test_3(self):
		#第3条：了解bytes、str与unicode的区别
		print("")

	def test_4(self):
		#第4条：用辅助函数来取代复杂的表达式
		print("")

	def test_5(self):
		#第5条：了解切割序列的办法
		print("")

	def test_6(self):
		#第6条：在单次切片操作内，不要同时指定start、end和stride
		print("")

	def test_7(self):
		#第7条：用列表推导来取代map和filter
		print("")

	def test_8(self):
		#第8条：不要使用含有两个以上表达式的列表推导
		print("")

	def test_9(self):
		#第9条：用生成器表达式来改写数据量较大的列表推导
		print("")

	def test_10(self):
		#第10条：尽量用enumerate取代range
		print("")

	def test_11(self):
		#第11条：用zip函数同时遍历两个迭代器
		print("")

	def test_12(self):
		#第12条：不要在for和while循环后面写else块
		print("")

	def test_13(self):
		#第13条：合理利用try/except/else/finally结构中的每个代码块
		print("")

