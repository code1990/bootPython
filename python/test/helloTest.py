def add(a, b):
    if isinstance(a, str):
        return a + '+' + b
    return a + b


def test_one():
    print("我是方法一")
    x = "this"
    assert "h" in x


def test_two():
    print("我是方法二")
    x = 5
    assert x > 6

class TestClass:
    def test_one(self):
        x="this"
        assert "h" in x

    def test_two(self):
        x="hello"
        assert  hasattr(x,"check")

    def test_three(self):
        a="hello"
        b="hello world"
        assert a in b

def hello():
    print("hello world")

if __name__=="__main__":
    hello()
    test_one()
    test_two()
