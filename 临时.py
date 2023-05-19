#这是一个平时测试的空文件
#这一行是git的测试
list1 = [1, 2, 2]
list2 = [1, 2]

diff_list = [x for x in list1 if x not in list2]

print("The difference between list1 and list2 is:", diff_list)

