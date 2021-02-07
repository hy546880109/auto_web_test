from page_objects import PageElement, PageObject ,MultiPageElement 


class Blog_Post_Page(PageObject):
    home_post = PageElement(css = '#menu-posts > a >.wp-menu-name')
    write_post = PageElement(css = '.page-title-action')
    write_post_alert = PageElement(css = 'div.components-modal__header > button > svg')
    write_post_title = PageElement(css = '#post-title-0')
    write_post_text = PageElement(css = '#post-content-0')
    write_post_release = PageElement(css = 'button.components-button.editor-post-publish-panel__toggle.editor-post-publish-button__button.is-primary')
    write_post_release_button = PageElement(css = 'div.editor-post-publish-panel__header-publish-button > button')
    post_release_status = PageElement(css = 'div.components-panel__body.post-publish-panel__postpublish-header.is-opened')
    


