# 断言 assert
# unittest 常见单元测试库
import unittest

from py_learn.TestTarget import LeeJohn,my_adder

# python -m unittest py_learn.TestClass  ( run in local console
class TestMyAdder(unittest.TestCase): # 测试方法必须以test_开头，这个库只会按照这个命名规则去搜索测试用例
    def setUp(self):# 在所有测试样例前执行，可以初始化测试用的对象
        self.obj = LeeJohn()

    def test_positive_add(self):
        # assert my_adder(5,3) == 8
        self.assertEqual(my_adder(5,4),19)

    def test_negative_add(self):
        assert my_adder(5,-5)==0
        self.assertTrue(9>1)
        self.assertNotIn(2,[13,3,23,-1])

    def test_method_in_obj(self):
        self.assertTrue(self.obj.compare_number(45,4))











