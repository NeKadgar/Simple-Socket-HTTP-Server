from utils import string_to_fstring
from urllib import parse


def main_page(url, html):
    with open(f"templates/{html}", "r") as file:
        document = string_to_fstring(file.read(), path=url.path)
    return document


def about_page(url, html):
    with open(f"templates/{html}", "r") as file:
        document = string_to_fstring(file.read(), path=url.path)
    return document


def post_page(url, html):
    try:
        post_id = parse.parse_qs(url.query)['id'][0]
    except KeyError:
        post_id = 0
    with open(f"templates/{html}", "r") as file:
        document = string_to_fstring(file.read(), path=url.path, id=post_id)
    return document


def error_page(url, html):
    with open(f"templates/{html}", "r") as file:
        document = string_to_fstring(file.read(), path=url.path)
    return document
