// const a = {
//   a: undefined,
//   b: null,
//   c: NaN,
//   d: () => {},
//   e: Symbol(),
// }

// console.log(JSON.stringify(a))
// export {}

const zip = (a: any[], b: any[]) =>
  Array.from({ length: Math.min(a.length, b.length) }, (_, i) => [a[i], b[i]])

const zipped = zip([1, 2, 3], ['a', 'b', 'c', 'd'])

console.log(Object.fromEntries(zipped))
