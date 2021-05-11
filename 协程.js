// Generator 函数可以暂停执行和恢复执行，这是它能封装异步任务的根本原因。
// Generator 函数就是一个封装的异步任务，或者说是异步任务的容器。异步操作需要暂停的地方，都用 yield 语句注明。
// Generator 函数是协程在 ES6 的实现，最大特点就是可以交出函数的执行权（即暂停执行）。
function* gen(x) {
  try {
    const y = yield x + 2
    console.log(y)
  } catch (error) {
    console.log(error)
  }
}

const g = gen(1)
// 激活协程，yield产出值
console.log(g.next())

// Generator 函数的数据交换和错误处理
// next 方法返回值的 value 属性，是 Generator 函数向外输出数据；相当于python的__next__()或者next(iterator)
// next 方法还可以接受参数，这是向 Generator 函数体内输入数据;输入的数据传入yield左侧，便于接下来异步函数取值调用。
// 相当于python的generator.send(value)
console.log(g.next(20))
console.log(g.next())

g.throw('出错了')

// Generator 函数的用法
// const fetch = require('node-fetch')

// function* gen() {
//   const url = 'https://api.github.com/users/github'
//   const result = yield fetch(url)
//   console.log(result.bio)
// }

// const g = gen()
// const result = g.next()

// result.value
//   .then(function (data) {
//     return data.json()
//   })
//   .then(function (data) {
//     g.next(data)
//   })
