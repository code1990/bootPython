# 第9章　类　　138
# 9.1　创建和使用类　　138
# 根据Dog 类创建的每个实例都将存储名字和年龄
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


# __init__() 是一个特殊的方法，每当你根 据Dog 类创建新实例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
# 根据类创建实例
# 调用Dog 类 中的方法__init__() 。方法__init__() 创建一个表示特定小狗的示例，并使用我们提供的值来设置属性name 和age 。方法__init__() 并未显式地包含return 语句， 但Python自动返回一个表示这条小狗的实例。
my_dog = Dog('willie', 6)
# 访问属性
print(my_dog.name)
# 调用方法
my_dog.sit()
my_dog.roll_over()
# 创建多个实例
your_dog = Dog('lucy', 3)


# 9.2　使用类和实例　　142
# 下面来编写一个表示汽车的类，它存储了有关汽车的信息
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #     给属性指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
# 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 通过方法修改属性的值
my_new_car.update_odometer(23)
my_new_car.read_odometer()
# 通过方法对属性的值进行递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


# 9.3　继承　　147
# 一个类继承 另一个类时，它将自动获得另一个类的所有属性和方法；原有的 类称为父类 ，而新类称为子类 。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # super() 是一个特殊函数，帮助Python将父类和子类关联起来。
        # 父类也称为超类 （superclass），名称super因此而得名
        # 父类的方法__init__() ，让ElectricCar 实例包含父类的所 有属性
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())


# 让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。
# 重写父类的方法
# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写
# 可以将大型类拆分成多个协同工作的小类
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# 9.4　导入类　　
# 导入模块中的所有类
# from module_name import *
# 9.5　Python标准库　　
# Python标准库 是一组模块，安装的Python都包含它。
# 9.6　类编码风格　　
# 类名应采用驼峰命名法 ，即将类名中的每个单词的首字母都大写
# 实例名和模块名都采用小写格式，并在单词之间加上下划线。
