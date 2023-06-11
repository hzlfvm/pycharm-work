import qrcode

# 创建 QRCode 对象，并指定需要生成二维码的内容
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,  # 设置错误纠正等级为 Q
)

qr.add_data("CSDN@墨城烟柳ベ旧人殇\n我的主页是：https://blog.csdn.net/weixin_51496226?spm=1000.2115.3001.5343")  # 内容
qr.make(fit=True)  # 生成可以使用 make_image() 方法创建图像的 QR 码图案

# 生成图片，并保存到本地文件
img = qr.make_image(fill_color="black", back_color="#F5DEB3")  # 设置填充色为黑色，背景颜色为 "#F5DEB3"（淡褐色）
img.save("1.jpg")
