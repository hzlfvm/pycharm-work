import re
import random
import tkinter as tk
from tkinter import ttk


def manchester_encode(bits: str) -> str:
    """曼切斯特编码"""
    encoded_data = ""
    for bit in bits:
        if bit == '0':
            encoded_data += '01'
        else:
            encoded_data += '10'
    return encoded_data


def add_noise(encoded_data: str, noise: str) -> str:
    """添加噪声"""
    encoded_data = list(encoded_data)
    index = random.randint(0, len(encoded_data))  # 生成随机索引
    encoded_data.insert(index, noise)  # 在随机位置插入噪音
    return ''.join(encoded_data)  # 列表转字符串


def check_collision(encoded_data: str) -> bool:
    """碰撞检测"""
    if "000" in encoded_data or "111" in encoded_data:
        return True
    else:
        return False


def test_encoding() -> None:
    """测试编码"""
    bits = input_box.get().strip()
    # 如果复选框被选中，则获取噪声输入，且判断是否输入合法
    noise = noise_box.get().strip() if noise_var.get() == 1 else None
    output_text.set("")  # 清空输出文本框

    # 使用正则表达式判断输入是否合法
    if not re.match("^[01]+$", bits):
        output_text.set("请输入仅由0和1组成的数据！")
        return

    encoded_bits = manchester_encode(bits)
    output_text.set(f"原始数据: {bits}\n"
                    f"曼切斯特编码: {encoded_bits}\n")

    if noise is not None:
        # 使用正则表达式判断输入是否合法
        if not re.match("^[01]+$", noise):
            output_text.set("请输入仅由0和1组成的数据！")
            noise_box.delete(0, tk.END)  # 清空噪声输入框
            return
        noisy_bits = add_noise(encoded_bits, noise)
        output_text.set(f"{output_text.get()}加入的噪声: {noise}\n"
                        f"加入噪声后的编码: {noisy_bits}\n"
                        f"编码是否碰撞: {'碰撞了' if check_collision(noisy_bits) else '未碰撞'}\n")
    else:
        output_text.set(f"{output_text.get()}编码是否碰撞: {'碰撞了' if check_collision(encoded_bits) else '未碰撞'}\n")

    # 画出编码图
    canvas.delete("all")
    x, y = 20, 50
    for i, bit in enumerate(encoded_bits):
        if bit == "0":
            canvas.create_line(x, y, x+20, y, width=2, fill="black")
            canvas.create_line(x+20, y, x+20, y+20, width=2, fill="black")
            canvas.create_line(x+20, y+20, x+40, y+20, width=2, fill="black")
            canvas.create_line(x+40, y+20, x+40, y, width=2, fill="black")
            canvas.create_line(x+40, y, x+60, y, width=2, fill="black")
        else:
            canvas.create_line(x, y+20, x+20, y+20, width=2, fill="black")
            canvas.create_line(x+20, y+20, x+20, y, width=2, fill="black")
            canvas.create_line(x+20, y, x+40, y, width=2, fill="black")
            canvas.create_line(x+40, y, x+40, y+20, width=2, fill="black")
            canvas.create_line(x+40, y+20, x+60, y+20, width=2, fill="black")
        x += 60


def clear_output() -> None:
    """清空输出文本框"""
    input_box.delete(0, tk.END)
    noise_box.delete(0, tk.END)
    noise_check.deselect()
    output_text.set("")
    canvas.delete("all")


# 创建窗口和组件
window = tk.Tk()
window.title("曼切斯特")

style = ttk.Style(window)
style.theme_use('vista')

input_label = ttk.Label(window, text="输入数据：")
input_label.pack(fill='x', padx=5, pady=5)

input_box = ttk.Entry(window, width=30)
input_box.pack(padx=5, pady=5)

noise_var = tk.IntVar(value=0)
noise_check = ttk.Checkbutton(window, text="添加噪声", variable=noise_var, command=lambda: noise_box.config(
    state=tk.NORMAL) if noise_var.get() == 1 else noise_box.config(state=tk.DISABLED))
noise_check.pack(fill='x', padx=5, pady=5)

noise_label = ttk.Label(window, text="噪声：")
noise_label.pack(fill='x', padx=5, pady=5)

noise_box = ttk.Entry(window, width=10, state=tk.DISABLED)
noise_box.pack(padx=5, pady=5)

output_text = tk.StringVar()
output_label = ttk.Label(window, textvariable=output_text, justify=tk.LEFT, wraplength=280)
output_label.pack(pady=5, padx=5)

button_frame = ttk.Frame(window)
button_frame.pack(fill='x')

run_button = ttk.Button(button_frame, text="运行", command=test_encoding)
run_button.pack(side=tk.LEFT, padx=5, pady=5)

clear_button = ttk.Button(button_frame, text="清除", command=clear_output)
clear_button.pack(side=tk.LEFT, padx=5, pady=5)

# 添加画布
canvas = tk.Canvas(window, width=700, height=100)
canvas.pack(fill='x', padx=5, pady=5)

# 绑定事件
noise_check.bind("<Button-1>", lambda e: noise_box.focus())

window.mainloop()