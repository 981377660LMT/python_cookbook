a = 1
b = 2
c = 2
d = []
if a or ((b + 1) == c):
    print('go to left')
else:
    print('go to right')

if d:
    print('list不为空')

# 新代码
account = 'qiyue'
password = '123456'

print('please input account')
user_account = input()

print('please input password')
user_password = input()

if account == user_account and password == user_password:
    print('success')
else:
    print('fail')
