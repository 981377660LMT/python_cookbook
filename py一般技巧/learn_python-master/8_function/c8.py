def seqsum(*param):
    sum = 0
    for i in param:
        sum += i * i
    print(sum)


seqsum(1, 2, 3)
