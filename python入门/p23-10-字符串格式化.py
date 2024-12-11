#   通过占位形式完成拼接
name="姚磊"
message="在硅谷工作%s"%name
            #   用  %  进行字符串的拼接
print(message)
print("\n")

# 通过字符串的形式完成数字和字符串的拼接
moey=18888
day=20
message1="我在硅谷工作了%d天,赚了%d元"%(day,moey)
print(message1)
print("\n")

#  案例
name2="传智播客"
year=2006
moey2=19.99
message2="%s成立于%d年,今日股价%f元"%(name2,year,moey2)
print(message2)
print("\n")
print("%s成立于%d年,今日股价%f元"%(name2,year,moey2))

"""
%s    字符串 (采用str()的显示)
%r    字符串 (采用repr()的显示)
%c    单个字符
%b    二进制整数
%f    浮点型
%d    十进制整数
%i    十进制整数
%o    八进制整数
%x    十六进制整数
"""