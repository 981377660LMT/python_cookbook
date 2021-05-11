import os
# with open('somefile.txt', 'r') as t:
#     for line in list(t)[:2]:
#         print(line)

print((os.path.join(os.path.dirname(__file__), 'somefile.txt')))
