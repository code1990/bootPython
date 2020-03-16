# 第11章　测试代码　　187
# 使用Python模块unittest 中的工具来测试代码
# 11.1　测试函数　　187
def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()


def get_formatted_name2(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


# 单元测试和测试用例
#
# Python标准库中的模块unittest 提供了代码测试工具。
# 单元测试 用于核实函数的某个方面没有问题；
# 测试用例 是一组单元测试，这些单元测试一起核实函数在各种情形下的 行为都符合要求。
# 良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。
# 全覆盖式测试 用例包含一整套单元测试，涵盖了各种可能的函数使用方 式。
# 对于大型项目，要实现全覆盖可能很难。
# 通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。


# 先导入模块unittest 以及要测试的函 数，再创建一个继承unittest.TestCase 的类，
# 并编写一系列方法对函数行为的不同方面进行测试
import unittest


# 最好让它看起来与要测试的函数相关，并包含字样Test
class NamesTestCase(unittest.TestCase):
    # 以test 打头的方法都将自动运行。
    # 如果你检查的条件没错，测试通过了意味着函数的行为是对的，而测试未通过意味着你编写的新代码有错
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        # 断言方法用来核实得到的结果是否与期望的结果一致。
        # 如果你检查的条件没错，测试通过了意味着函数的行为是对的，而测试未通过意味着你编写的新代码有错。
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name2('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()


# 11.2　测试类　　193
# 1　各种断言方法
# 方法	用途
# assertEqual(a, b)	核实a == b
# assertNotEqual(a, b)	核实a != b
# assertTrue(x)	核实x 为True
# assertFalse(x)	核实x 为False
# assertIn(item , list )	核实 item 在 list 中
# assertNotIn(item , list )	核实 item 不在 list 中
class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)


class TestAnonmyousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    # 如果你在TestCase 类中包含了方法setUp() ，Python将先运行它，再运行各个以test_打头的方法。
    def test_store_single_response(self):
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # my_survey.store_response('English')
        # self.assertIn('English', my_survey.responses)
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
