const prices = { ACME: 45.23, AAPL: 612.78, IBM: 205.55, HPQ: 37.2, FB: 10.75 }

console.log(Object.fromEntries(Object.entries(prices).filter(([_, value]) => value > 200)))
export {}
