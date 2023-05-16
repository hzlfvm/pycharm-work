import numpy as np


# 明文分组，返回明文向量列表
def split_text(text, m):
    text_len = len(text)
    remainder = text_len % m

    # 如果明文长度不能整除m，则在末尾补全'a'
    if remainder != 0:
        text += 'a' * (m - remainder)

    vec_list = []

    # 每m个字符为一组，转换为数字映射后存储为向量
    for i in range(0, len(text), m):
        vec = []
        for j in range(m):
            vec.append(ord(text[i + j]) - ord('a'))
        vec_list.append(vec)
    return vec_list


# 矩阵转换为字母形式，返回字符串
def matrix_to_text(matrix):
    text = ''
    for vec in matrix:
        for elem in vec:
            text += chr(elem + ord('a'))
    return text


# 求矩阵的逆矩阵
def matrix_inverse(key_matrix):
    # 计算行列式的值
    det = key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]
    # 计算模26下的逆元
    inv_det = pow(int(det), -1, 26)
    # 计算伴随矩阵
    adj_matrix = np.array([[key_matrix[1][1], -key_matrix[0][1]], [-key_matrix[1][0], key_matrix[0][0]]])
    # 计算逆矩阵并返回
    return (inv_det * adj_matrix) % 26


# 加密函数
def encrypt(text, m, key_matrix):
    # 将明文分组成向量
    vec_list = split_text(text, m)
    # 将密钥矩阵转化为numpy数组
    key_matrix = np.array(key_matrix, dtype=int)
    # 将所有向量组成mxm的矩阵
    vec_matrix = np.array(vec_list).reshape(-1, m)
    # 进行矩阵运算，得到新向量
    new_vec_matrix = np.dot(vec_matrix, key_matrix) % 26
    # 转换为字母形式的密文
    cipher_text = matrix_to_text(new_vec_matrix)
    return cipher_text


# 解密函数
def decrypt(cipher_text, key_matrix):
    # 将密文分组成向量
    vec_list = split_text(cipher_text, len(key_matrix))
    # 将密钥矩阵转化为numpy数组，并求逆矩阵
    key_matrix = np.array(key_matrix, dtype=int)
    inv_key_matrix = matrix_inverse(key_matrix)
    # 将所有向量组成mxm的矩阵
    vec_matrix = np.array(vec_list).reshape(-1, len(key_matrix))
    # 进行矩阵运算，得到新向量
    new_vec_matrix = np.dot(vec_matrix, inv_key_matrix) % 26
    # 转换为字母形式的明文
    plain_text = matrix_to_text(new_vec_matrix)
    return plain_text


# 测试代码1
text = "friday"
print("明文:", text)
key_matrix = [[1, 7], [4, 7]]
m = len(key_matrix)

cipher_text = encrypt(text, m, key_matrix)
print("加密后的密文：", cipher_text)
plain_text = decrypt(cipher_text, key_matrix)
print("解密后的明文：", plain_text)

# 测试代码2
text = "meeth"
print("明文:", text)
key_matrix = [[11, 8], [3, 7]]
m = len(key_matrix)

cipher_text = encrypt(text, m, key_matrix)
print("加密后的密文：", cipher_text)
plain_text = decrypt(cipher_text, key_matrix)
print("解密后的明文：", plain_text)
