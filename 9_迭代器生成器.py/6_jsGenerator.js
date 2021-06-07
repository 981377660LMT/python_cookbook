function* gen() {
  const a = yield 1
  // return为迭代器的最后一次迭代（当done等于时true）提供返回值。
  return a * 2
}

const g = gen()

// console.log(g.next())
// console.log(g.next(3))

// # 如果使用for ... of循环或类似方法通过迭代器进行迭代Array.from，则该return值将被忽略
for (const item of g) {
  console.log(item)
}
