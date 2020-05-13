## 第1章　引论
建议1：理解Pythonic概念
建议2：编写Pythonic代码
建议3：理解Python与C语言的不同之处
建议4：在代码中适当添加注释
建议5：通过适当添加空行使代码布局更为优雅、合理
建议6：编写函数的4个原则
建议7：将常量集中到一个文件
## 第2章　编程惯用法
建议8：利用assert语句来发现问题
建议9：数据交换值的时候不推荐使用中间变量
建议10：充分利用Lazyevaluation的特性
建议11：理解枚举替代实现的缺陷
建议12：不推荐使用type来进行类型检查
建议13：尽量转换为浮点类型后再做除法
建议14：警惕eval()的安全漏洞
建议15：使用enumerate()获取序列迭代的索引和值
建议16：分清==与is的适用场景
建议17：考虑兼容性，尽可能使用Unicode
建议18：构建合理的包层次来管理module
## 第3章　基础语法
建议19：有节制地使用from...import语句
建议20：优先使用absoluteimport来导入模块
建议21：i+=1不等于++i
建议22：使用with自动关闭资源
建议23：使用else子句简化循环（异常处理）
建议24：遵循异常处理的几点基本原则
建议25：避免finally中可能发生的陷阱
建议26：深入理解None，正确判断对象是否为空
建议27：连接字符串应优先使用join而不是+
建议28：格式化字符串时尽量使用.format方式而不是%
建议29：区别对待可变对象和不可变对象
建议30：[]、()和{}：一致的容器初始化形式
建议31：记住函数传参既不是传值也不是传引用
建议32：警惕默认参数潜在的问题
建议33：慎用变长参数
建议34：深入理解str()和repr()的区别
建议35：分清staticmethod和classmethod的适用场景
## 第4章　库
建议36：掌握字符串的基本用法
建议37：按需选择sort()或者sorted()
建议38：使用copy模块深拷贝对象
建议39：使用Counter进行计数统计
建议40：深入掌握ConfigParser
建议41：使用argparse处理命令行参数
建议42：使用pandas处理大型CSV文件
建议43：一般情况使用ElementTree解析XML
建议44：理解模块pickle优劣
建议45：序列化的另一个不错的选择——JSON
建议46：使用traceback获取栈信息
建议47：使用logging记录日志信息
建议48：使用threading模块编写多线程程序
建议49：使用Queue使多线程编程更安全
## 第5章　设计模式
建议50：利用模块实现单例模式
建议51：用mixin模式让程序更加灵活
建议52：用发布订阅模式实现松耦合
建议53：用状态模式美化代码
## 第6章　内部机制
建议54：理解built-inobjects
建议55：__init__()不是构造方法
建议56：理解名字查找机制
建议57：为什么需要self参数
建议58：理解MRO与多继承
建议59：理解描述符机制
建议60：区别__getattr__()和__getattribute__()方法
建议61：使用更为安全的property
建议62：掌握metaclass
建议63：熟悉Python对象协议
建议64：利用操作符重载实现中缀语法
建议65：熟悉Python
建议66：熟悉Python
建议67：基于生成器的协程及greenlet
建议68：理解GIL的局限性
建议69：对象的管理与垃圾回收
## 第7章　使用工具辅助项目开发
建议70：从PyPI安装包
建议71：使用pip和yolk安装、管理包
建议72：做paster创建包
建议73：理解单元测试概念
建议74：为包编写单元测试
建议75：利用测试驱动开发提高代码的可测性
建议76：使用Pylint检查代码风格
建议77：进行高效的代码审查
建议78：将包发布到PyPI
## 第8章　性能剖析与优化
建议79：了解代码优化的基本原则
建议80：借助性能优化工具
建议81：利用cProfile定位性能瓶颈
建议82：使用memory_profiler和
建议83：努力降低算法复杂度
建议84：掌握循环优化的基本技巧
建议85：使用生成器提高效率
建议86：使用不同的数据结构优化性能
建议87：充分利用set的优势
建议88：使用multiprocessing克服GIL的缺陷
建议89：使用线程池提高效率
建议90：使用C/C++模块扩展提高性能
建议91：使用Cython