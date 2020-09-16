import random
import string


def get_domain_code(length):
    letters = '!#$&()*+,-.0123456789:;<?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^`}|{~'
    domain_code = ''.join(random.choice(letters) for i in range(length))
    return domain_code


def get_api_key(length):
    letters = string.ascii_lowercase + string.digits
    api_key = ''.join(random.choice(letters) for i in range(length))
    return api_key
