from queue import PriorityQueue as PQ

pq = PQ()

# 当一个对象的所有元素都是可比较的时，
# 默认情况下是根据队列中的对象的第一个元素进行排序，
# 越小的优先级越高，排在越前面。
# 当第一个元素相同时，依次比较后续的元素的大小来进行排序。
pq.put((1, 'a'))
pq.put((3, 'a'))
pq.put((2, 'a'))

print(pq.get())
print(pq.queue)

print(pq.qsize())  # 优先队列的尺寸

while not pq.empty():
    print(pq.get())
