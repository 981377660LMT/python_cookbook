# format_map的参数不需传入“关键字=真实值”，而是直接传入真实的字典值。我们来看个案例：
student = {'name': '小明', 'class': '20190301', 'score': 597.5}
s1 = '{st[class]}班{st[name]}总分：{st[score]}'.format(st=student)
s2 = '{class}班{name}总分：{score}'.format_map(student)
