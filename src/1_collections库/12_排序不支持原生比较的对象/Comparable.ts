type Comparable<T> = (...args: T[]) => number

interface IPerson {
  name: string
  age: number
}

const key: Comparable<IPerson> = (a, b) => a.age - b.age

export {}
