import random
from collections import Counter
list_colour=['♥','♣','♠','♦']                             #构造花色
list_num=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']             #构造值
list_card=[]                                              #构造牌

def create_card():
    for i in list_colour:
        for j in list_num:
            card=f"{i}{j}"
            list_card.append(card)
    return list_card

list_user=["张三","李四","王五","赵六"]                      #构造用户

#发牌
def fapai():
    random.shuffle(list_card)                   #洗牌，打乱列表的顺序
    user_cards = {}                             #可以使用字典存储每个用户的组
    for i in list_user:
        cards = []                              #值是一个列表对象
        for _ in range(3):
            card = list_card.pop()              #取出列表里面的最后一个元素并从列表删除
            cards.append(card)
        user_cards[i] = cards                   #存放到值的列表中
    return user_cards

#改变部分牌的值
def change(a):
    if a=='J':
        a=11
    if a=='Q':
        a=12
    if a=='K':
        a=13
    if a=='A':
        a=14
    return a

#判断单子
def danzi(list):
    result=0.1*list[0]+1*list[1]+10*list[2]         #[2,3,A]=143.2  [10,Q,K]=143
    return result

#判断对子
def duizi(list):
    if len(set(list))==2:                             #说明有对子
        counts = Counter(list)
        most_common_element = counts.most_common(1)[0][0]      #要知道重复的是哪个元素,这里元素的最大次数肯定是2
        least_common_element = counts.most_common()[-1][0]     #最少的元素既是单独的哪个元素
        result=most_common_element*100+least_common_element*1  #最大单子：[J,K,A]=143.2,最小对子:[2,2,3]=203
        return result
    else:
        return 0

#判断顺子
def shunzi(list):
    if (list[1]-list[0]==1) and (list[2]-list[1]==1):                 #说明有顺子
        result=list[2]*300+list[1]*100+list[0]*10                    #最小顺子：[2,3,4]=1520,最大对子：[K,A,A]=1413
        return result
    else:
        return 0

#判断同花顺
def simlar_colour_shunzi(list1,list2):
    if (list1[1]-list1[0]==1)and(list1[2]-list1[1]==1):
        if list2[0]==list2[1]==list2[2]:
            reslut=list1[2]*1000+list1[1]*500+list1[0]*100
            return reslut
        else:
            return 0
    else:
        return 0

#判断豹子
def baozi(list):
    if list[0]==list[1]==list[2]:                                         #最大同花顺：[Q,K,A]=21700,最小豹子：[2,2,2]=30000
        result=list[0]*15000
        return result
    else:
        return 0


#测试代码
create_card()                          #初始化，生成牌
user_cards = {}
user_cards = fapai()                                #发牌
print(user_cards)
zuihou=[]
for i in list_user:
    list=user_cards.get(i)              #取出每张牌
    a=list[0]
    b=list[1]
    c=list[2]
    card_a=(a[1:])
    card_b=(b[1:])
    card_c=(c[1:])
    card_a = change(card_a)
    card_b = change(card_b)
    card_c = change(card_c)
    value=[int(card_a),int(card_b),int(card_c)]
    sorted_value=sorted(value)
    colour_a = (a[0:1])
    colour_b = (b[0:1])
    colour_c = (c[0:1])
    colour=[colour_a,colour_b,colour_c]
    result1=danzi(sorted_value)
    result2=duizi(sorted_value)
    result3=shunzi(sorted_value)
    result4=simlar_colour_shunzi(sorted_value,colour)
    result5=baozi(sorted_value)
    result=[result1,result2,result3,result4,result5]
    zuihou.append(result)
print(zuihou)
jieguo1=sorted(zuihou[0])
jieguo2=sorted(zuihou[1])
jieguo3=sorted(zuihou[2])
jieguo4=sorted(zuihou[3])
a=jieguo1[4]
b=jieguo2[4]
c=jieguo3[4]
d=jieguo4[4]
value=sorted([a,b,c,d])
print(value)
if value[3]==a:
    print(f"{list_user[0]}赢了")
if value[3]==b:
    print(f"{list_user[1]}赢了")
if value[3]==c:
    print(f"{list_user[2]}赢了")
if value[3]==d:
    print(f"{list_user[3]}赢了")
















