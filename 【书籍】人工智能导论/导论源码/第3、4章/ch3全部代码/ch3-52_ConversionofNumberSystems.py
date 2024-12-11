#ch3-52_ConversionofNumberSystems
def int2base(n, base): 
    result = []
    div = n
    while div != 0: 
        div, mod = divmod(div, base)
        result.append(mod)
    result.reverse()    
    result = ''.join(map(str, result))
    return eval(result)
print(int2base(80,2))
print(int2base(80,8))
print(int2base(80,16))
print(int2base(80,13))

