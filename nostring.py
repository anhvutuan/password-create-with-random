#!/usr/bin/python3
import string
import itertools

result = []
count = 0
char = 6

try:
    letters = string.ascii_letters + string.ascii_letters
    for i in range(0, len(letters) + 1):
        for _combine in itertools.combinations(letters, i):
            if len(_combine) < char:
                continue
            if len(_combine) > char:
                break
            count += 1
            result.append("".join(_combine))
except:
    print(f"Has issues but completed: {count} password with {char} character")
finally:
    print(f"Completed: {count} password with {char} character")
    with open("generate_password.txt", "w+") as _f:
        for _password in result:
            _f.write(_password + "\n")
