from urllib import parse
from views import main_page, about_page, post_page, error_page


urls = (
        ("/", "index.html", main_page),
        ("/about", "about.html", about_page),
        ("/post", "post.html", post_page)
    )


class URL:
    @staticmethod
    def parse(url):
        url = parse.urlparse(url)
        for url_, html, func in urls:
            if url_ == url.path:
                return func(url, html)
        return error_page(url, "error.html")
