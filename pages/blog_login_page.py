from page_objects import PageElement, PageObject ,MultiPageElement 

class Blog_Login_Page(PageObject):
    '''登陆页面'''
    login_user = PageElement(id_ = 'user_login')
    login_passwd = PageElement(id_ = 'user_pass')
    login_jizhu = PageElement(id_ = 'rememberme')
    login_button = PageElement(id_ = 'wp-submit')

