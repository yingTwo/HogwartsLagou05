
def provider():
    for i in range(3):
        print("开始操作")
        yield i
        print("结束操作")

p = provider()
for i in p:
    print(i)
