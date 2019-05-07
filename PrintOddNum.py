import re


class Person:
    name = []
    print("Person Class:"+str(name))


tom = Person()
print(tom.name)
tom.name.append("tom")
print(tom)
print(Person.name)

a = 1
while a < 100:
    print(a)
    a = a + 1
citylist = ["shanghai", "hangzhou", "huzhou", "beijing", "nanchang"]
for i in citylist:
    print(i)
print(citylist[0])
print(citylist[0] == "shanghai")
city = "shanghai"

if citylist[0] == "shanghai":
    print("citylist contain shanghai", end="|")
else:
    print("citylist dont contain  shanghai")
str1 = "你好$$$我正在学 Python@#@现在需要&*&*&修改字符串"
str2 = str1.replace('$$$', ' ').replace('@#@', ' ').replace('&*&*&', ' ')
print("\n")
print(str1, end="@@@")
print(str2)

str2 = re.sub('[@#$&*]+', '', str1)
print(str2)
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d\t" % (j, i, i * j), end="|")  # 不想换行就加end=" "
    print("")
x = float(input("please input one number: "))
y = float(input("please input one number: "))
print("%f*%f=%f" % (x, y, x * y))


def cal_profit(i):
    if i <= 10:
        print("利润为10万时,应发放奖金总数为%f万元" % (i * 10 / 100), end=" ")
    elif 20 >= i > 10:
        print("利润为20万时,应发放奖金总数为%f万元" % ((i - 10) * 7.5 / 100 + 10 * 10 / 100), end=" ")
    elif 40 >= i > 20:
        print("利润为40万时,应发放奖金总数为%f万元" % ((i - 20) * 3 / 100 + 20 * 10 / 100 + 10 * 7.5 / 100), end=" ")
    elif 60 >= i > 20:
        print("利润为60万时,应发放奖金总数为%f万元" % ((i - 10) * 75 / 100 + 10 * 10 / 100), end=" ")


cal_profit(20)

print("\n")


def cal_profit_a(i):
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, 6):
        if i > arr[idx]:
            r = r + (i - arr[idx]) * rat[idx]
            i = arr[idx]
    return r


i = int(input("please input profit of this year : "))
profit = cal_profit_a(i)
print("利润为%d时,奖金可得%d" % (i, profit), end="")
