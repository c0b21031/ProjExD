import random
a="サザエさんの旦那の名前は?"
b="カツオの妹の名前は？"
c="タラオはカツオから見てどんな関係"
lst=[a,b,c]
kaito=input(random.choice(lst))
if kaito==a:
    if kaito=="マスオ":
        print("正解")
    else:
        print("はずれ")

if kaito==b:
    if kaito=="ワカメ":
        print("正解")
    else:
        print("はずれ")

if kaito==c:
    if kaito=="甥":
        print("正解")
    else:
        print("はずれ")
