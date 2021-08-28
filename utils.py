def string_to_fstring(non_f_str: str, *args, **kwargs):
    return eval(f'f"""{non_f_str}"""')