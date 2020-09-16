import random


def get_domain_code(length):
    letters = '!#$&()*+,-.0123456789:;<?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^`}|{~'
    domain_code = ''.join(random.choice(letters) for i in range(length))
    return domain_code
