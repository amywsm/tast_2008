# print("hello world")
# # # print("hello world")
# a="hello world"
# print(a)
# l = [1,2,3,4,5]
# l[0] = 10
# print(l)
#
# t = (1,23,4)
#
# print(t[0]);
#
#
# s = {9,2,2,34}
# print(s)
#
# a = 10
# b = "12"
# print(a + int(b));
# print(str(a) + b);
# a = 30
# b = "22.2"
# print(a + float(b));
# print(str(a) + b);
# a = True
# b = 1
# print(a + b);
# d = {"name":"哈哈","age":18}
# print(d);
# print(d["name"]);
#
# l = [1,2,3,4]
# print(tuple(l));
# print(set(l));
# t = (1,2,3,4)
# print(list(t));
# print(set(t));
# s = {1,2,3,4}
# print(list(s));
# print(tuple(s));
# a = "123"
# print(list(a));
# print(tuple(a));
# print(set(a));

# #成员运算符 in    not in
# a = "asdfg"
# l = ["a","2","g"]
# t = ("a","3","g")
# s = {"a","4","g"}
# d = {"a","5","g"}
# d = {"name":"王大锤","age":12}
# print("a"in a);
# #print("a"in l);
# print("a"in t);
# print("a"in s);
# print("a"in d);
# print("name"in d);

# # 如果我有10000万
#
# money = 10000
#
# if(money >= 10000):
#     print("买两万豆浆，喝一碗仍一碗")
# else:
#     print("洗洗睡吧")
#
# #如果我有20000 30000
#
# money = 2000000
# if(money <20000):
#     print("买两碗豆浆")
# elif(money < 30000):
#     print("仍一碗喝一碗")
# # else:
#     print("洗洗睡吧")
# # 循环for
# for i in [1,2,3,4,5]:
#     print("重要的事情要说100遍",end="\n");
# for i in range(5):
#     print("重要的事情要说100遍");

# # 循环函数
# print((list(range(10))))
# print((list(range(1,10))))
# print((list(range(1,10,2))))
# print((list(range(10,0,-2))))
# print((list(range(10,0,-1))))

# #  while循环
# i = 5
# while(i < 7):
#     print(i)
#     i += 1;

# #  打印1-11 的数字，遇到6不打印 continue（是跳过成立的条件 so:6， 打印不成立的数字）
# for i in range(1,11):
#     if(i == 6):
#         continue
#     print(i)

# break 是结束循环  continue 是跳过成立的循环

# # 函数方法 def 定义一个自定义函数; div 方法名; a b指外界参数 必须写在括号里面；
# def div(a,b):
#     if(b == 0):
#         print("被除数不能为零")
#     else:
#         print(a /b)
# div(10,20)
# div(80,40)

# # return 结束方法
# def select_data(sql):
#     ser = "查询结果"
#     return ser
# result = select_data("hhhh")
# print(result)

# # 参数定义  位置参数  关键字参数
#
# def res (a,b):
#     return a + b
#     print(res(1,3));
#
# def res(a,b=3):
#     return a+b
# print(res(1,3));
#
#
# def res(a,b=3):
#     return a-b
# print(res(1,3));
#
# # # 动态参数
# def a(*args,**argss):
#     print(args)
#     print(argss)
# a(1,2,3,4,a=6,b=7);
#
# def a(*args,**argss):
#     return (a,b)
#     print(args)
#     print(argss)
# a(1,2,3,4,a=6,b=7);
#
# def a(a,*args,b=3,**argss):
#     print(a)
#     print(b)
#     print(args)
#     print(argss)
# a(1,2,3,4,c=6,b=7);

# #  写入文件
# f = open("aa,txt",'w')
# f.write("good")
# f.close();


#  全局 局部 ；局部需要global
# c = 48
# def ccc ():
#     global c
#     c = 23
# ccc()
# print(c);
#
# # # 全局
# c = 48
# #def ccc ():
#     c = 23
# ccc()
# print(c);


# #a = "123456"
# print(a[-3:])
# print(a[1:3])
# print(a[1:-1])
# print(a[2:5:2])
# #  # 去除空格
# a = " adbc "
# print(a.strip())
# table = "姓名,性别,年龄"
# table = table.replace(",",">")
# print(table)
# # print(table.split(','))
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{} x {} = {}".format(j,i,i*j),end="\t")
#     print()

# l = [1,2,3,4,5,6]
# l[0] = 20
# #print(l)
# l.append(7)
# print(l)
# l.insert(3,8)
# # print(l)
#
# p2 = [8,99,4,7,1]
# # p2.sort(reverse=True)
# # print(p2)
#
# sorted(p2)
# print(sorted(p2))

# # 类 和对象
#
# class str_medo():
#     class1 = None
#     def replace(self):
#         print("111111111111111111")
#     def split(sekf):
#         print("222222222")
# sm = str_medo()
# sm.c = "hello"
# sm.replace()
# sm.split()
# 方法
class str_demo():
    def __init__(self):
        print("魔法方法")

    def replace(self):
        print("实例方法")
        pass

    @classmethod
    def split(cla):
        print("类方法")

    @staticmethod
    def static():
        print("静态方法")

str_demo();
str_demo().replace();
str_demo.split();
str_demo().static();

 # 类的封装

class privatedemo():
    __c = None
    def set_a(self,value):
        self.__a = value
    def get_a(self):
        return self.__a
p =  privatedemo()
p.set_a("hello")
print(p.get_a())



#  报错处理

print("asdfgh")
try:
#    r = open("module_4.py","r")
    print(1/2)
except(FileNotFoundError,ZeroDivisionError) as e:
    print(e)
    print("程序执行遇到了问题")
    print("重新打开文件")
#print("文件重新打开")
except(ZeroDivisionError) as e:
    print(e)
else:
    print("程序没有报错")
finally:
    print("程序都会执行")
print("文件已经打开")



















































































