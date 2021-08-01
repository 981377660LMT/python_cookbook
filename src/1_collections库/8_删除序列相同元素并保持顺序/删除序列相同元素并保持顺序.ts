// forEach内不能yield
function* dedupe<D>(items: D[], key?: (arg: D) => any) {
  const visited = new Set<D>()

  for (const item of items) {
    const val = key ? key(item) : item
    if (!visited.has(val)) yield item
    visited.add(val)
  }
}

const arr = [1, 5, 2, 1, 9, 11, 1, 5, 10]
const objArr = [
  { x: 2, y: 3 },
  { x: 1, y: 4 },
  { x: 2, y: 3 },
  { x: 2, y: 5 },
  { x: 10, y: 15 },
]

console.log(Array.from(dedupe(arr)))
console.log(Array.from(dedupe(objArr, (obj: { [x: string]: any }) => `${obj['x']}#${obj['y']}`)))

// js没有必要 因为 set去重不会打乱顺序 而python会
