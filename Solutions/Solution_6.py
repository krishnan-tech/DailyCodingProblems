def is_char(code):
    return 0 if code > 26 or code < 1 else 1

def get_message_count(code):
    code_str = str(code)
    if len(code_str) == 1:
        count = 1
    elif len(code_str) == 2:
        count = 1 + is_char(code)
    else:
        count = get_message_count(int(code_str[1:]))
        if is_char(int(code_str[:2])):
            count += get_message_count(int(code_str[2:]))

    return count
