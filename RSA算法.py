import random
import base64

# 定义一个函数用于生成指定位数的素数
def creat_number(num1,num2):
    while True:
        p = random.randint(num1,num2)           #随机产生一个指定位数的整数
        if checknum(p):
            return p
        #一直while循环，直到产生的数是素数

# 判断是否为素数
def checknum(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    #如果循环结束还没有数与之整除，这个数就是素数
    return True

# 计算扩展欧几里得算法（求逆元）
def niyuan(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = niyuan(b % a, a)
        return (g, x - (b // a) * y, y)
#参数a:模数，参数b：需求逆元的数，返回值中g是a和b的最大公约数，x - (b // a) * y这个式子的值就是我们所求的逆元

#产生公钥和私钥函数
def creatkey(p,q):
    n=p*q                  #计算n=p*q
    ln=(p-1)*(q-1)         # 计算φ(n) = (p-1) * (q-1)
    e = 65537              # 选择一个与ln互质的整数e作为公钥指数,一般都选取65537相当于约定俗成
    # 计算d = e^(-1) mod ln，即e模ln的逆元
    _, d, _ = niyuan(e, ln)
    # 确保d在合法范围内（1 < d < ln）
    d = d % ln
    if d <= 1:
        d += ln
    # 返回公钥(n, e)和私钥d
    return n, e, d

#加密函数
def encrypt(message, n, e):
    print("Alice发送使用公钥加密后的密文为：", end='')
    encrypted_list = []
    for char in message:
        encrypted_num = pow(ord(char), e, n)       #利用pow函数进行RSA加密
        encrypted_char = chr(encrypted_num)        #转化为ASCll字符
        encrypted_list.append(encrypted_char)      #存入列表
    encrypted_message = ''.join(encrypted_list)    #拼接成一个字符串
    # 进行 Base64 编码
    base64_data = base64.b64encode(encrypted_message.encode('utf-8')).decode('ascii')
    print(base64_data)          #编码结果即密文
    return base64_data


#解密函数
def decrypt(value,n,d):
    print("Bob收到Alice发送的密文：",end='')
    print(value)
    # 进行 Base64 解码
    binary_data = base64.b64decode(value)        #解码得到二进制数字
    binary_string = binary_data.decode('utf-8')  #换成ASCll字符串
    decrypted_list = []
    for i in range(len(binary_string)):
        decrypted_num = pow(ord(binary_string[i]), d, n)        #利用pow函数进行RSA解密
        decrypted_char = chr(decrypted_num)                     #换成字符串
        decrypted_list.append(decrypted_char)
    decrypted_message = ''.join(decrypted_list)
    print("Bob利用私钥解密结果为：",end='')
    print(decrypted_message)


#测试代码
a=input("请输入产生素数的范围起点：")
num1=int(a)
b=input("请输入产生素数的范围终点：")
num2=int(b)
p=creat_number(num1,num2)
q=creat_number(num1,num2)
c=input("请输入Alice要发送给Bob的明文：")
str1=list(c)
n,e,d=creatkey(p,q)
str2=encrypt(str1,n,e)
print("------------------")
decrypt(str2,n,d)
