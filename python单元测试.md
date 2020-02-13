检查pip的版本
```shell
pip --version
```
更新pip
```
python -m pip install --upgrade pip
```
安装pytest
```
pip install -U pytest
```

查看安装的版本

```
pytest --version
```



# 编写pytest测试样例的规则

- 测试文件以test_开头（以_test结尾也可以）
- 测试类以Test开头，并且不能带有 **init** 方法
- 测试函数以test_开头
- 断言使用基本的assert即可



**pycharm 配置pytest单元测试模块一直 报错 修改使用main方法的方式去执行**