name="传智播客"  #公司名称
date_moeny=19.99  # 股价
gp_number="003032"  # 股票代码
mr_date=1.2  # 增长系数
day=7       # 增长天数
jg=date_moeny * mr_date ** day
print(f"公司名称:{name}股票代码:{gp_number}当前股价:{date_moeny}""\n")
print(f"每日增长系数:{mr_date}经过{day}天后的股价是:{round(date_moeny * (mr_date ** day), 2)}")
        #第二种写法
print(f"每日增长系数:{mr_date}经过{day}天后的股价是:%.2f" % jg)

