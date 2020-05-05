# 非布尔值逻辑运算
a = 'hello'
b = []

print(a and b)# []

print(a or b) # hello

print(not b)  # True

print( not a) # False

print(type(range(20)))
print(type(b))
# 断言
# assert b == None , 'b 不为 false'

a = [1,2,3]
b =(1,)
c = (a in b)
# 问题：c是不是元组
print('==={0}'.format(type(c))) # ===<class 'bool'>
print(b in a) #false

a1 = [(1,),(1,2,),(1,2,3)]
print(type(a1)) # class list
print(b in a1) # true

a2 = {(1,),(1,2),(1,2,3)}
print(type(a2)) # <class 'set'>
print(b in a2) # True