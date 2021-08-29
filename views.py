from utils import load_page
from urllib import parse


def main_page(url, html):
    return load_page(html, params={'path': url.path})


def about_page(url, html):
    return load_page(html, params={'path': url.path})


def post_page(url, html):
    post_id = parse.parse_qs(url.query).get('id')
    if post_id:
        return load_page(html, params={'path': url.path, 'post_id': post_id[0]})
    return error_page(url, "error.html")


def error_page(url, html):
    return load_page(html, params={'path': url.path})
