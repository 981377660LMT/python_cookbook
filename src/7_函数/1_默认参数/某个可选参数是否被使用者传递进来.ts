const identityB = Symbol.for('b')

const foo = (a: number, b: string | Symbol = identityB) => {
  if (b === identityB) {
    console.log('没传b')
  } else {
    console.log('传了b')
  }
}

foo(1)
foo(1, 'a')
