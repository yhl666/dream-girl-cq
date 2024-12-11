# 1.使用print直接输出类型信息
print("第一种方法")
print("数据类型",type("姚磊"))
print("数据类型",type(123))
print("数据类型",type(123.45))

print("\n")  # 换行打印 \n
# 2.使用变量存储type()语句的结果
print("第二种方法")
sj1_type=type("姚磊666")
sj2_type=type(123)
sj3_type=type(123.45)
print("数据类型",sj1_type)
print("数据类型",sj2_type)
print("数据类型",sj3_type)

# 3.使用type()语句，查看变量中的存储的数据类型信息
print("\n")
print("第三种方法")
name="姚磊888"
name_sj=type(name) # 使用一个变量把type()存储起来
print("数据类型",name_sj) # 输出这个变量
name2=123
name2_sj=type(name2)
print("数据类型",name2_sj)
name3=123.45
name3_sj=type(name3)
print("数据类型",name3_sj)
#!/usr/bin/python3 
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
'''

