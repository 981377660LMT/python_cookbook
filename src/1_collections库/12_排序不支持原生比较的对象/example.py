from operator import attrgetter

# 内置的 sorted() 函数有一个关键字参数 key ，可以传入一个 callable 对象给它
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


# Example
users = [User(23), User(3), User(99)]
print(users)

# Sort it by user-id
print(sorted(users, key=attrgetter('user_id')))

# attrgetter() 函数通常会运行的快点，并且还能同时允许多个字段进行比较
