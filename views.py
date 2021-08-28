from utils import load_page
from urllib import parse


def main_page(url, html):
    return load_page(html, params={'path': url.path})


def about_page(url, html):
    return load_page(html, params={'path': url.path})


def post_page(url, html):
    try:
        post_id = parse.parse_qs(url.query)['id'][0]
    except KeyError:
        post_id = 0
    return load_page(html, params={'path': url.path, 'post_id': post_id})



def error_page(url, html):
    return load_page(html, params={'path': url.path})

