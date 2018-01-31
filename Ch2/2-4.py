# 列表推导可以直接生成迪卡尔积 列表推导只可以生成列表
print([(i, j) for i in ('A', 'B') for j in ('1', '2')])


# 生成器表达式最外面是园括号 如果作为函数参数，则不需要园括号
# 生成器只是生成一个可以迭代的对象，而不需要一次就产生所有的值，避免占用内存
print((i for i in range(10)))
for j in (i for i in range(11)):
    print(j)

# _作为占位符
for i, _ in ((1, 'a'), (2, 'b')):
    print(i)

print(divmod(20, 8))
t = (20, 8)
# *运算符可以把一个可迭代对象拆开，作为函数的参数
print(*t)
a, b = divmod(*t)
print(a, b)
