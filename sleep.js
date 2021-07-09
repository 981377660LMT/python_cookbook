const sleep = async () =>
  await new Promise(resolve => {
    setTimeout(() => {
      resolve()
      console.log(666)
    }, 1000)
  })

sleep()

console.log(1)
