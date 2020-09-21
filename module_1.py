# def speak():
#     print("我是模块1")
# speak()




#1、编写一个返回随机手机号的方法
# import random
# def random_phone():
#     l = random.choices("0123456789", k=9)
#     a = random.choice("358")
#     s = "".join(l)
#     print("1"+a+s)
# random_phone()


#2、编写一个返回指定长度和内容的随机字符串方法
# import random
# def len_sstr(num,str):
#     l = random.choices(str,k=random.randint(1,3))
#     s = "".join(l)
#     print(s)
# len_sstr(5,"asdfgh")

 #3、编写一个返回随机姓名的方法
# import random
# def name(str):
#     l = random.choices(str,k=1)
#     s = "".join(l)
#     print(s)
# name("王大锤")

# #3、编写一个返回随机姓名的方法
# import random
# def name(str1,str2):
#     l = random.choices(str1,k=1)
#     m = random.choices(str2, k=random.randint(1,3))
#     s = "".join(l)
#     f = "".join(m)
#     print(s+f)
#
# str1 = "王吴刘周"
# str2 = "尚美上没事"
# name(str1,str2)










