import random

# 参数设置
tatal = 1000  # 发送时间范围
length = 1  # 帧长
solt = 1  # 时隙
num = 1000  # 总帧数
list = []  # 用来存放每一个数据帧


# 帧类
class Frame:
    def __init__(self, name, time):
        self.name = name  # 帧的名字
        self.send_time = time  # 帧的发送时间


# 随机产生每个帧的发送时间
for i in range(num):
    # 帧的名字用序号代替，发送时间都是整数
    name = i
    send_time = random.randrange(0, tatal + 1, solt)
    frame = Frame(name, send_time)
    list.append(frame)

# 按发送时间属性排序(按时间发送)
list.sort(key=lambda x: x.send_time)  # lambda定义了一个隐含函数x,该函数返回send_time属性


success = 0  # 成功发送帧的数量
conflict = 0  # 发生冲突即本轮传输失败的帧数量

# 有帧发送、并且发送时间在通信时间内才发送
while len(list) > 0 and list[0].send_time <= tatal:
    current_frame = list[0]  # 当前帧一直都是list[0]

    # 冲突检测
    address = []  # 存放冲突帧的name

    # 所有冲突帧存储到address,没有则len(address)=1
    for i in range(len(list)):
        if list[i].send_time == current_frame.send_time:
            address.append(i)

    # 没有冲突,移除列表，同时成功发送帧数量加1
    if len(address) == 1:
        list.remove(current_frame)
        success += 1

    # 发生冲突
    else:
        for i in address:
            list[i].send_time += random.randint(1, tatal + 1) * solt  # 延迟发送时间k个时隙
        conflict += 1  # 冲突帧的数量加1
        list.sort(key=lambda x: x.send_time)  # 重新排序
        address.clear()

# 计算吞吐率
z = success / num
# 输出
print("通信时间:", tatal, "帧长:", length)
print(f"成功发送的帧数量:{success}")
print(f"发送的帧总数量:{num}")
print(f"冲突次数:{conflict}")
print(f"吞吐率:{z}")
