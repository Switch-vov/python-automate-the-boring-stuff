import re


def checkPassword(password):
    passwordReg = re.compile(r'''
        (?=^.{8,}$)     # 八位数及以上
        ((?=.*\d+))     # 至少一位数字
        (?![.\n])       # 没有换行符
        (?=.*[A-Z])     # 大写任意个
        (?=.*[a-z]).*$  # 小写任意个
    ''', re.VERBOSE)

    match = passwordReg.match(password)
    return match is not None


print(checkPassword('A'))  # False
print(checkPassword('a'))  # False
print(checkPassword('1'))  # False
print(checkPassword('Aa'))  # False
print(checkPassword('A1'))  # False
print(checkPassword('a1'))  # False
print(checkPassword('Aa1'))  # False
print(checkPassword('Aa12345'))  # False
print(checkPassword('AaBbCcDd'))  # False
print(checkPassword('ABCD1234'))  # False
print(checkPassword('abcd1234'))  # False
print(checkPassword('Aa123456'))  # True
