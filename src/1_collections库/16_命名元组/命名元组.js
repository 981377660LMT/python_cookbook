'use strict'

const vm = require('vm')

function stripIndent(source) {
  return source.replace(/^ {1,4}/gm, '')
}

/**
 *
 * @param {string} name
 * @returns
 * @description Object.freeze 模拟元组不可更改
 */
function createNamedTuple(name) {
  const props = Array.from(arguments).slice(1)
  const source = stripIndent(`
    'use strict'

    class ${name} {
      constructor (${props.join(', ')}) {
        ${props.map(a => `this.${a} = ${a}`).join('\n        ')}
        Object.freeze(this)
      }
    }

    ${name}.prototype[Symbol.iterator] = function* () {
      ${props.map(a => `yield this.${a}`).join('\n      ')}
    }

    ${name}
  `)

  return vm.runInNewContext(source)
}

module.exports = createNamedTuple

/////////////////////////////////////////////////////
const Point = createNamedTuple('Point', 'x', 'y')
const p = new Point(12, 16)
console.log(p.x)
console.log(Point.toString())
console.log(...p)
console.log(Point.prototype[Symbol.iterator].toString())
