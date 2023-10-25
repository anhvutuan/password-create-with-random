#!/usr/bin/python3
import random
import string

generate_password = lambda x: ''.join([random.choice(string.ascii_letters + string.hexdigits) for _ in range(x)])

line = 1000 * int(1e3) # Number one created (1 * 1000) = 1000 line
character = 6          # Number char password

list_password = [generate_password(character) for _ in range(line)]

with open('generate_password', 'w+') as _f:
    for _password in list_password:
        _f.write(_password + "\n")

print(f'Đã tạo {line} password, thành công')