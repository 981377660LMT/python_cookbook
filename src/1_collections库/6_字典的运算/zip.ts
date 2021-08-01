const obj = {
  ACME: 45.23,
  AAPL: 612.78,
  IBM: 205.55,
  HPQ: 37.2,
  FB: 10.75,
}

console.log(
  Object.entries(obj)
    .map<[number, string]>(([a, b]) => [b, a])
    .sort((a, b) => a[0] - b[0])
)
