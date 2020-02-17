# unittest框架使用总结
# 二、unittest工作原理
#
# unittest中最核心的四部分是：TestCase，TestSuite，TestRunner，TestFixture
# （1）一个TestCase的实例就是一个测试用例。
# 测试用例就是指一个完整的测试流程，包括测试前准备环境的搭建（setUp），执行测试代码（run），
# 以及测试后环境的还原（tearDown）。
#
# （2）而多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite。
#
# （3）TestLoader是用来加载TestCase到TestSuite中的。
#
# （4）TextTestRunner是来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法
#
# （5）测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息。
import unittest


class MyUT(unittest.TestCase):
    # 2、每个测试方法均以test开头，否则不能被unittest识别
    def test_1(self):
        print("test-1")

    def test_2(selfs):
        print("test-2")

    @classmethod
    def run_suite(cls):
        suite = unittest.TestSuite()
        suite


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyUT('test_1'))
    suite.addTest(MyUT('test_2'))
    suite.run()

# 九、总结
#
# 1、unittest是python自带的单元测试框架，我们可以用其来作为我们自动化测试框架的用例组织执行框架。
#
# 2、unittest的流程：写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中，我们通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例。
#
# 3、一个class继承unittest.TestCase即是一个TestCase，其中以 test 开头的方法在load时被加载为一个真正的TestCase。
#
# 4、verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告。
#
# 5、可以通过addTest和addTests向suite中添加case或suite，可以用TestLoader的loadTestsFrom__()方法。
#
# 6、用 setUp()、tearDown()、setUpClass()以及 tearDownClass()可以在用例执行前布置环境，以及在用例执行后清理环境
#
# 7、我们可以通过skip，skipIf，skipUnless装饰器跳过某个case，或者用TestCase.skipTest方法。
#
# 8、参数中加stream，可以将报告输出到文件：可以用TextTestRunner输出txt报告，以及可以用HTMLTestRunner输出html报告。

# https://www.jianshu.com/p/e7cf427468c8

# unittest case的运行流程：
#
# 写好一个完整的TestCase
# 多个TestCase 由TestLoder被加载到TestSuite里面, TestSuite也可以嵌套TestSuite
# 由TextTestRunner来执行TestSuite，测试的结果保存在TextTestResult中
# TestFixture指的是环境准备和恢复
# unittest中最核心的部分是：TestFixture、TestCase、TestSuite、TestRunner
#
# Test Fixture
# 用于测试环境的准备和恢复还原, 一般用到下面几个函数。
#
# setUp()：准备环境，执行每个测试用例的前置条件
# tearDown()：环境还原，执行每个测试用例的后置条件
# setUpClass()：必须使用@classmethod装饰器，所有case执行的前置条件，只运行一次
# tearDownClass()：必须使用@classmethod装饰器，所有case运行完后只运行一次
# Test Case
# 参数verbosity可以控制错误报告的详细程度：默认为1。0，表示不输出每一个用例的执行结果；2表示详细的执行报告结果。
# Verbosity=1情况下成功是 .，失败是 F，出错是 E，跳过是 S
# 测试的执行跟方法的顺序没有关系, 默认按字母顺序
# 每个测试方法均以 test 开头
# Verbosity=2情况下会打印测试的注释
#
# Test Suite
# 一般通过addTest()或者addTests()向suite中添加。case的执行顺序与添加到Suite中的顺序是一致的
#
# @unittest.skip()装饰器跳过某个case
# （1）skip():无条件跳过
# @unittest.skip("i don't want to run this case. ")
# （2）skipIf(condition,reason):如果condition为true，则 skip
# @unittest.skipIf(condition,reason)
# （3）skipUnless(condition,reason):如果condition为False,则skip
# @unittest.skipUnless(condition,reason)
#
# Test Loder
# TestLoadder用来加载TestCase到TestSuite中。
# loadTestsFrom*()方法从各个地方寻找testcase，创建实例，然后addTestSuite，再返回一个TestSuite实例
# defaultTestLoader() 与 TestLoader()功能差不多，复用原有实例
#
# Testing Report
# 终端报告： 如上terminal 分支
# TXT报告： 如上txt 分支，当前目录会生成ut_log.txt文件
# HTML 报告：如上html 分支，终端上打印运行信息同时会在当前目录生成report文件夹， 文件夹下有test.html和test.log文件
#
