# Example:  Modified non-recursive implementation using
# a special Visit() class to signal what should be visited next

# 避免递归的一个通常方法是使用一个栈或队列的数据结构。 例如，深度优先的遍历算法，第一次碰到一个节点时将其压入栈中，处理完后弹出栈。
# 你也许想去寻找其它没有yield语句的方案
# 如果不使用生成器，代码会变得很臃肿，到处都是栈操作语句、回调函数等。
# 实际上，使用yield语句可以让你写出非常漂亮的代码，它消除了递归但是看上去又很像递归实现，代码很简洁。

import types


class Node:
    pass


class Visit:
    def __init__(self, node):
        self.node = node


class NodeVisitor:
    def visit(self, node):
        stack = [Visit(node)]
        last_result = None
        while stack:
            print(last_result)
            try:
                last = stack[-1]
                # yield一个generator
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                # yield一个Visitor,访问者模式处理Visitor
                elif isinstance(last, Visit):
                    stack.append(self._visit(stack.pop().node))
                # yield一个数字
                else:
                    last_result = stack.pop()
            except StopIteration:
                print(stack)
                stack.pop()
        return last_result

    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    # yield一个generator 外面调用send返回值是数字
    def visit_Add(self, node):
        yield ((yield Visit(node.left)) + (yield Visit(node.right)))

    def visit_Sub(self, node):
        yield ((yield Visit(node.left)) - (yield Visit(node.right)))

    def visit_Mul(self, node):
        yield ((yield Visit(node.left)) * (yield Visit(node.right)))

    def visit_Div(self, node):
        yield ((yield Visit(node.left)) / (yield Visit(node.right)))

    def visit_Negate(self, node):
        yield -(yield Visit(node.operand))


if __name__ == '__main__':
    # 1 + 2*(3-4) / 5
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)

    # Evaluate it
    e = Evaluator()
    print(e.visit(t4))  # Outputs 0.6

    # Blow it up

    # a = Number(0)
    # for n in range(1, 100000):
    #     a = Add(a, Number(n))

    # try:
    #     print(e.visit(a))
    # except RuntimeError as e:
    #     print(e)

