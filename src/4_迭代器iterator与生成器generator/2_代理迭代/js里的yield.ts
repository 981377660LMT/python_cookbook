// The yield* expression is used to delegate to another generator or iterable object.
function* bar() {
  yield 2
  yield 3
  yield 4
}

function* foo(...args: any[]) {
  yield 1
  yield* [1, 2]
  yield* bar()
  yield* '34'
  yield* Array.from(arguments)
}

const iter = foo(1, 2, 3)
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
console.log(iter.next())
for (const item of iter) {
  console.log(item)
}

export {}
