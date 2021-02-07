import unittest
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from pages.blog_delete_page import Blog_Post_Page
from test_login_blog import Test_Blog

# @unittest.skip('跳过删除博客用例')
class Test_delete_blog(Test_Blog):
    '''删除博客测试用例'''

    def test_delete_blog_success(self):
        delete_blog = Blog_Post_Page(self.driver)
        delete_blog.home_post.click()
        mouse = delete_blog.delect_post_locat
        ActionChains(self.driver).move_to_element(mouse).perform()
        blog_title_old = delete_blog.delect_post_button
        bt = blog_title_old[0].text
        blog_title_old[0].click()
        blog_title_new = delete_blog.delect_post_button
        bt2 = blog_title_new[0].text
        assert bt != bt2, '文章未删除成功'


if __name__ == '__main__':
    unittest.main()
