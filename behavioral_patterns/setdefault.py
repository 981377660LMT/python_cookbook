a = {}
# nsert key with a value of default if key is not in the dictionary.

# Return the value for key if key is in the dictionary, else default.
# 如果 key 不在字典中，则插入值为 default 的 key。
# 如果键在字典中，则返回键的值，否则返回默认值。
a.setdefault('a', []).append(1)
print(a)

