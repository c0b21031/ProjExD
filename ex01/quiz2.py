import random
import datetime

alphabet_num=10
abs_alphabet_num=3

all_alphabet_list=[chr(i) for i in range(97, 97+26)]
alphabet_list=random.sample(all_alphabet_list,alphabet_num)


print(f"対象文字{alphabet_list}")


abs_list=[]
for i in range(abs_alphabet_num):
    abs_list.append(alphabet_list.pop(i))

print(f"表示文字:{alphabet_list}")

kaito=int(input("欠損文字はいくつあるでしょうか?"))

if kaito==abs_alphabet_num:
    print("正解")
    for i in range(abs_alphabet_num):
        kaito2=input(f"{i+1}つ目の文字を入力してください")
        if kaito2 in abs_list:
            abs_list.remove(kaito2)
            print("正解!")
        else:
            print("不正解")

            break
    print("全問正解おめでとう!")

else:
    print("不正解")


