import random

# 仿真参数设置
t = 1000  # 通信时间
length = 1  # 帧长
total = 1000  # 发送总数


# 数据帧类
class Frame:
    def __init__(self, time):
        self.send_time = time  # 发送时间


# 存储所有数据帧的列表，列表可边循环边增删等操作
list0 = []

# 随机产生数据帧
for i in range(total):
    send_time = random.uniform(0, t+1)
    frame = Frame(send_time)
    list0.append(frame)

# 按发送时间属性排序(按时间发送)
list0.sort(key=lambda x: x.send_time)

success = 0  # 成功发送的帧数量
num = 0  # 记录冲突次数

# 有帧发送并且在通信时间范围内(生成的帧都在t内，但冲突延时后的帧不一定)就发送，否则通信结束
while len(list0) > 0 and list0[0].send_time <= t:
    current_frame = list0[0]  # 当前数据帧

    # 冲突检测
    index = []  # 冲突帧的位置列表
    # 所有冲突帧存储到index,没有则len(index)=1，即存储当前帧的位置
    for j in range(len(list0)):
        if list0[j].send_time - current_frame.send_time < length:
            index.append(j)

    if len(index) == 1:  # 没有冲突
        list0.remove(current_frame)
        success += 1

    else:  # 发生冲突
        for frame in index:
            list0[frame].send_time += random.uniform(0.1, t+1)  # 延迟发送时间
        num += 1
        list0.sort(key=lambda x: x.send_time)  # 重新排序
        index.clear()

# 计算吞吐率
S = success / total

# 输出
print(f"通信时间:{t},帧长:{length}")
print(f"成功发送的帧数量:{success}")
print(f"发送的帧总数量:{total}")
print(f"冲突次数:{num}")
print(f"吞吐率:{S}")
