# 加密函数
def encrypt(plaintext, a, b):
    """
    仿射密码加密函数
    :param plaintext: 明文，字符串类型(小写)
    :param a: 加密参数a，整数类型，要求gcd(a, 26) = 1，0<=a<=25
    :param b: 加密参数b，整数类型,0<=b<=25
    :return: 密文，字符串类型
    """
    cipher_text = ""
    # 转小写字母
    plaintext = plaintext.lower()
    for char in plaintext:
        # 将字母转化为0-25的数字
        char_num = ord(char) - ord('a')
        # 加密算法
        char_num = (a * char_num + b) % 26
        # 将0-25的数字转化为小写字母
        cipher_text += chr(char_num + ord('a'))
    return cipher_text


# 解密函数
def decrypt(ciphertext, a, b):
    """
    仿射密码解密函数
    :param ciphertext: 密文，字符串类型
    :param a: 加密参数a，整数类型，要求gcd(a, 26) = 1
    :param b: 加密参数b，整数类型
    :return: 明文，字符串类型
    """

    # 计算a的逆元，即求(a * x) % 26 == 1 的整数 x
    # 也可以自定义扩展欧几里得算法计算
    a_inv = pow(a, -1, 26)
    plain_text = ""
    for char in ciphertext:
        # 将字母转化为0-25的数字
        char_num = ord(char) - ord('a')
        # 解密算法
        char_num = (a_inv * (char_num - b)) % 26
        # 将0-25的数字转化为小写字母
        plain_text += chr(char_num + ord('a'))
    return plain_text


# 测试代码1
plain_text = "Hello"
a = 7
b = 3
cipher_text = encrypt(plain_text, a, b)
print("加密结果为：", cipher_text)
plain_text_decrypt = decrypt(cipher_text, a, b)
print("解密结果为：", plain_text_decrypt)

# 测试代码2
plain_text = "hot"
a = 7
b = 3
cipher_text = encrypt(plain_text, a, b)
print("加密结果为：", cipher_text)
plain_text_decrypt = decrypt(cipher_text, a, b)
print("解密结果为：", plain_text_decrypt)
