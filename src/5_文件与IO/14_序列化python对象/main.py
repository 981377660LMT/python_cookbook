# 你需要将一个Python对象序列化为一个字节流，以便将它保存到一个文件、存储到数据库或者通过网络传输它。
# 对于序列化最普遍的做法就是使用 pickle 模块
# dump(object, file)
# dumps(object) -> string
# load(file) -> object
# loads(string) -> object

import pickle

data = {"cmnx": 'a'}

# 将一个对象保存到一个文件中
with open('somefile', 'wb') as f:
    pickle.dump(data, f)

# 将一个对象转储为一个字符串
s = pickle.dumps(data)

# Restore from a file
with open('somefile', 'rb') as f:
    data = pickle.load(f)
    print(data)

# Restore from a string
data = pickle.loads(s)
print(data)
