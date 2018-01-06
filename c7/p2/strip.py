import re


def strip(text, chars=None):
    """去除首尾的字符

    :type text: string
    :type chars: string
    :rtype: string
    """
    if chars is None:
        reg = re.compile('^ *| *$')
    else:
        reg = re.compile('^[' + chars + ']*|[' + chars + ']*$')
    return reg.sub('', text)


print(strip('   123456   '))  # 123456
print(strip('   123456'))  # 123456
print(strip('   123456'))  # 123456
print(strip('123456   654321'))  # 123456   654321
print(strip('123456   654321', '1'))  # 23456   65432
print(strip('123456   654321', '1234'))  # 56   65
print(strip('123456   654321', '124'))  # 3456   6543
