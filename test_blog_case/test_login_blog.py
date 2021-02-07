from pages.blog_login_page import Blog_Login_Page
import unittest
from selenium import webdriver

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)


username = passwd = 'pyse_24'
url = 'http://139.199.192.100:8000/wp-login.php'


class Test_Blog(unittest.TestCase):
    '''博客测试用例前置和后置'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        blog_home = Blog_Login_Page(self.driver)
        blog_home.login_user.send_keys(username)
        blog_home.login_passwd.send_keys(passwd)
        blog_home.login_jizhu.click()
        blog_home.login_button.click()

    def tearDown(self):
        self.driver.quit()


class Test_login(Test_Blog):
    '''博客登陆测试用例'''

    def test_login_success(self):
        title_url = self.driver.current_url
        assert 'wp-admin' in title_url, '登陆不成功或者断言错误'


if __name__ == '__main__':
    unittest.main()
