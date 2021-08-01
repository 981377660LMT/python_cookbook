function* range(start: number, stop: number, increment: number) {
  let s = start

  while (s < stop) {
    // yield s
    s += increment
  }
}

// 不断调用next
for (const n of range(0, 4, 0.5)) {
  console.log(n)
}
