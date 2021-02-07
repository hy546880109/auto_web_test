import unittest
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
print(path)
print(sys.path)

from test_blog_case.test_login_blog import Test_login

if __name__ == '__main__':
    # 根据给定的测试类，获取其中所有以test开头的测试方法，并返回一个测试套件
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test_login)

    # 将多个测试类加载到测试套件中
    suite = unittest.TestSuite([suite1])

    # 设置verbosity = 2，可以打印出更详细的执行信息
    unittest.TextTestRunner(verbosity=2).run(suite)