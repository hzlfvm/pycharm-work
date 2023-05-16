def crc(str1: str, str2: str) -> dict:
    """自定义CRC计算校验码"""
    # str1附加len(str2)-1个0
    str = str1 + '0' * (len(str2) - 1)
    # 循环异或
    while len(str) >= len(str2):
        # 计算机进行模2运算，默认右对齐，而这里进行异或需要左对齐
        # 确保异或前左对齐(无前缀0)，每次计算str需要左移多少位
        length = len(str) - len(str2)
        temp = int(str, 2) ^ (int(str2, 2) << length)
        # 每次异或结果str转二进制字符串(自动去除前缀0b)
        # bin函数的结构为一个以‘0b’开始的字符串，我们进行切割，只需要后面的数值即可
        str = bin(temp)[2:]
    # 补全校验码的有效位数为k-1
    k = len(str2)
    crc_len = k - 1
    crc_str = str.zfill(crc_len)
    # 返回一个字典，包含计算出来的校验码和发送的数据
    result = {'a': crc_str, 'b': str1 + crc_str}
    return result


l1 = crc('101011001', '11001')
print(f"校验码:{l1['a']},发送的数据是{l1['b']}")
print('----------------------')
l2 = crc('1011001', '11001')
print(f"校验码:{l2['a']},发送的数据是{l2['b']}")
