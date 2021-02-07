from page_objects import PageElement, PageObject ,MultiPageElement 


class Blog_Post_Page(PageObject):
    home_post = PageElement(css = '#menu-posts > a >.wp-menu-name')
    delect_post_locat = PageElement (css = 'td.author.column-author > a')
    delect_post_button = MultiPageElement (css = 'td.title.column-title.has-row-actions.column-primary.page-title > div.row-actions > span.trash > a')
