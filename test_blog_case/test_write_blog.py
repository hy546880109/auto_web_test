import unittest
import uuid
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from pages.blog_write_page import Blog_Post_Page
from test_login_blog import Test_Blog


uid = str(uuid.uuid1())
suid = ''.join(uid.split('-'))


class Test_write_blog(Test_Blog):
    '''写博客测试用例'''
    def test_write_blog_success(self):

        write_blog = Blog_Post_Page(self.driver)
        write_blog.home_post.click()
        write_blog.write_post.click()
        write_blog.write_post_alert.click()
        write_blog.write_post_title.send_keys(suid)
        write_blog.write_post_text.send_keys(suid)
        write_blog.write_post_release.click()
        write_blog.write_post_release_button.click()
        blog_status = write_blog.post_release_status

        assert '已被发布' in blog_status.text, '文章未发布或断言错误'


if __name__ == '__main__':
    unittest.main()
