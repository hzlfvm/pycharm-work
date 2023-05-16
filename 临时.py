import random
from sympy import isprime

def modinv(a, m):
    """计算a关于模数m的模反元素"""

    def egcd(a, b):
        """扩展欧几里得算法，用于计算最大公约数和系数"""
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y

    g, x, y = egcd(a, m)
    if g != 1:
        # 如果模反元素不存在，则引发异常
        raise ValueError("modular inverse does not exist")
    else:
        # 返回结果，但结果可能是负数，确保最终结果落在[0, m)之间
        return x % m


def generate_prime_number(num_digits):
    """生成指定位数的素数"""
    while True:
        # 生成范围在10^(n-1)到10^n之间的随机数
        num = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
        # 确保num为奇数(提高找到范围内质数的效率)
        num |= 1
        # 是否是素数
        if isprime(num):
            return num


def keys(num):
    """生成密钥"""
    p = generate_prime_number(num)
    # 使得p和q的差距不超过一个数量级,并且p!=q
    q = generate_prime_number(num + 1)
    while p == q:
        q = generate_prime_number(num + 1)
    n = p * q
    # 计算欧拉函数
    pin = (p - 1) * (q - 1)
    # 公钥指数
    e = 65537
    # 求模反元素d
    d = modinv(e, pin)
    # 公钥和私钥
    return (n, e), (n, d)


# 第一次身份标识认证
def idTest(listsystem, ID):
    # 验证身份标识
    for item in listsystem:
        if item == ID:
            print(f"{ID}身份标识验证成功!")
            return True
        else:
            print(f"{ID}身份标识认证失败!")
            return False


# 第2/3次认证函数
def identify(first, second, public_key, private_key):
    """first验证second"""
    # first随机生成一个随机数R，发送给second
    R = random.randint(100, 10000)
    # first收到R，对其加密，发送给second
    R_modify = encrypt(public_key, R)
    # first收到R_modify，对其解密，看是否与R相等
    if decrypt(private_key, R_modify) == R:
        print(f"{first}验证{second}成功!")
        return True
    else:
        print(f"{first}验证{second}失败!")
        return False


def encrypt(public_key, plaintext):
    """RSA加密"""
    n, e = public_key
    ciphertext = pow(plaintext, e, n)
    # 返回的是数字，还需要处理
    return ciphertext


def decrypt(private_key, ciphertext):
    """RSA解密"""
    n, d = private_key
    plaintext = pow(ciphertext, d, n)
    # 返回的是数字，还需要处理
    return plaintext


# ------------------------A向B发送认证-----------------------

system = ['A', 'B', 'C', 'D']  # 系统中的阅读器身份标识

# 生成A的一对的密钥(速度较慢，这里位数用小一些演示)
public_keyA, private_keyA = keys(20)
print(f"公钥A:{public_keyA}")
print(f"私钥A:{private_keyA}")

# 生成B的一对的密钥
public_keyB, private_keyB = keys(20)
print(f"公钥B:{public_keyB}")
print(f"私钥B:{private_keyB}")

# 三次认证
result = False  # 当前验证结果
if idTest(system, 'A'):  # 第一次认证成功
    if identify('B', 'A', public_keyB, private_keyB):  # 第二次也认证成功
        result = identify('A', 'B', public_keyA, private_keyA)  # 第三次验证

# ----------认证成功：测试A对比B发送消息----------------------------

print("--------------------------------------------------------")
if result:
    """
        下方用编码的方式实现字符串和整数的互转。
        字符串str需要符合编码格式
    """
    # 消息
    str = "RSA identify"
    print(f"消息:{str}")
    message = str.encode('ascii')  # 用ascii编码为字节

    # 生成B的一对新的密钥(速度较慢，这里位数用小一些演示)
    public_key, private_key = keys(20)
    print(f"公钥B:{public_key}")
    print(f"私钥B:{private_key}")

    # 加密,A使用B的公钥对明文加密
    message_num = int.from_bytes(message, byteorder='big')  # 字节转整数，大端存储
    ciphertext_num = encrypt(public_key, message_num)  # 得到的密文数字
    print(f"加密-密文数字:{ciphertext_num}")

    # 解密,B使用B的密钥对密文解密
    plaintext_num = decrypt(private_key, ciphertext_num)  # 得到的明文数字
    plaintext = plaintext_num.to_bytes((plaintext_num.bit_length() + 7) // 8, byteorder='big').decode('ascii')  # 整数转字节然后用ascii解码
    print(f"解密-明文:{plaintext}")
