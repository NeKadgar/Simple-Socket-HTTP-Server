def string_to_fstring(non_f_str: str, params):
    return eval(f'f"""{non_f_str}"""')


def load_page(html, params):
    with open(f"templates/{html}", "r") as file:
        return string_to_fstring(file.read(), params=params)