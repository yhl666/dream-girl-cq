# 1.定义的三种方式
name='姚磊'   #单引号定义
print(type(name))
name2="姚磊1"   #双引号定义
print(type(name2))
name3="""姚磊666"""     #三引号定义
print(type(name3))
print("\n")

# 2.引号的嵌套
name4='"牛逼"'  #单引号包括双引号
print(name4)    #输出  "牛逼"
name5="'牛逼'"  #双引号包括单引号
print(name5)    #输出  '牛逼'
print("\n")

#   3.转义字符 \
#使用转义字符 \ 解除引号的效用
name6="\"牛逼\""
print(name6)
name7='\'牛逼\''
print(name7)