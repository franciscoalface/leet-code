# def reverse_string(s: list) -> list:
#     return s.reverse()


def reverse_string(s: list) -> list:
    if len(s) > 1:
        return [s[-1]] + reverse_string(s[:-1])
    return s
