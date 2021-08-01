with open('sample.txt', 'a') as f:
    print("ok", file=f)
# 文件必须是以文本模式t打开。 如果文件是二进制模式b的话，打印就会出错。
