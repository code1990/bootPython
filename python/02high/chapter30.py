# Python 面向对象

# 面向对象技术简介
# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
# 局部变量：定义在方法中的变量，只作用于当前实例的类。
# 实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
# 实例化：创建一个类的实例，类的具体对象。
# 方法：类中定义的函数。
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

# 创建类
# 使用 class 语句来创建一个新类，class 之后为类的名称并以冒号结尾:
class Employee:
    "员工的基类"
    empCount = 0  # empCount 变量是一个类变量 使用 Employee.empCount 访问

    def __init__(self, name, salary):  # 类的构造函数或初始化方法
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):  # self 代表类的实例，self 在定义类的方法时是必须有的，在调用时不必传入相应的参数
        print("total count", Employee.empCount)

    def displayEmployee(self):
        print("name", self.name, "salary", self.salary)

# self代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
class Test:
    # self 代表的是类的实例，代表当前对象的地址，
    # 而 self.__class__ 则指向类
    def prt(self):
        print(self)
        print(self.__class__)

t= Test()
t.prt()

# 创建实例对象
# 类的实例化类似函数调用方式。
emp1 = Employee("zara",2000)
emp2 = Employee("mike",2000)
# 访问属性
# 您可以使用点号 . 来访问对象的属性。使用如下类的名称访问类变量:
emp1.displayCount()
emp2.displayEmployee()
print(emp1.empCount)

# 你可以添加，删除，修改类的属性，如下所示：
emp1.age=10
emp1.age=12
del emp1.age # 删除对象的属性

# 使用以下函数的方式来访问属性：
#
# getattr(obj, name[, default]) : 访问对象的属性。
# hasattr(obj,name) : 检查是否存在一个属性。
# setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
# delattr(obj, name) : 删除属性。

hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
emp1.age=18
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age')    # 删除属性 'age'

# Python内置类属性
# __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
# __doc__ :类的文档字符串
# __name__: 类名
# __module__: 类定义所在的模块
# __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__dict__)

# python对象销毁(垃圾回收)
# Python 使用了引用计数这一简单技术来跟踪和回收垃圾。
# 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的，
# 由解释器在适当的时机，将垃圾对象占用的内存空间回收。
# Python 的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。

# 实例
# 析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"销毁")

pt1= Point()
pt2=pt1
pt3=pt1
print(id(pt1))
print(id(pt2))
print(id(pt3))
del pt1
del pt2
del pt3


# 类的继承
# 面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。
#
# 通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
# 在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。
# 区别在于类中调用普通函数时并不需要带上 self 参数
class Parent:
    parentAttr=100
    def __init__(self):
        print("调用父类的构造方法")

    def parentMethod(self):
        print("调用父类的一般方法")

    def setAttr(self,attr):
        Parent.parentAttr=attr

    def getAttr(self):
        print("父类属性:",Parent.parentAttr)

class Child(Parent):# 继承父类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类方法")

c= Child()# 实例化子类
c.childMethod()#子类调用子类的方法
c.parentMethod()#调用父类的一般方法
c.setAttr(200)
c.getAttr()

# 可以继承多个类
# class C(A, B):   # 继承类 A 和 B

# 你可以使用issubclass()或者isinstance()方法来检测。
# issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
# isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。


# 方法重写
# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：
class Parent1:
    def myMethod(self):
        print("调用父类方法")

class Child(Parent):
    def myMethod(self):
        print("调用子类方法")

c=Child() #实例化子类
c.myMethod() #子类调用重写后的父类方法

# 基础重载方法
# __init__ ( self [,args...] ) 构造函数
# __del__( self )   析构方法, 删除一个对象
# __repr__( self ) 转化为供解释器读取的形式
# __str__( self ) 用于将值转化为适于人阅读的形式
# __cmp__ ( self, x ) 对象比较


class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return "Vector(%d,%d)" %(self.a,self.b)

    def __add__(self, other):
        return Vector(self.a+other.b,self.b+other.b)

v1=Vector(2,10)
v2=Vector(5,-2)
print(v1+v2)

# 类属性与方法
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。
# 在类内部的方法中使用时 self.__private_attrs。
# 类的方法
# 在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
#
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。
# 在类的内部调用 self.__private_methods

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount=0#公开变量

    def count(self):
        self.__secretCount+=1
        self.publicCount+=1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount) # 报错，实例不能访问私有变量

# Python不允许实例化的类访问私有数据，
# 可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性
class TestInfo:
    __site="test"

test = TestInfo()
print(test._TestInfo__site)

# 单下划线、双下划线、头尾双下划线说明：
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
#
# _foo: 以单下划线开头的表示的是 protected 类型的变量，
# 即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
#
# __foo: 双下划线的表示的是私有类型(private)的变量,
# 只能是允许这个类本身进行访问了。


