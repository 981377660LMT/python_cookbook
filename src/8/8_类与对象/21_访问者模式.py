# 处理由大量不同类型的对象组成的复杂数据结构，每一个对象都需要进行不同的处理。
# 比如，遍历一个树形结构，然后根据每个节点的相应状态执行不同的操作。
# 解析DOM树???
# 假设你要写一个表示数学表达式的程序，那么你可能需要定义如下的类
class Node:
    pass


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


# Representation of 1 + 2 * (3 + 4) / 5
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)
# 这样做的问题是对于每个表达式，每次都要重新定义一遍，
# 有没有一种更通用的方式让它支持所有的数字和操作符呢。
# 这里我们使用访问者模式可以达到这样的目的：


class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


# 为了使用这个类，可以定义一个类继承它并且实现各种 visit_Name() 方法，其中Name是node类型。
class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return -node.operand


e = Evaluator()
print(e.visit(t4))

############################

# getattr() 来获取相应的方法，并利用递归来遍历所有的节点
# 这种技术也是实现其他语言中switch或case语句的方式
class HTTPHandler:
    def handle(self, request):
        methname = 'do_' + request.request_method
        getattr(self, methname)(request)

    def do_GET(self, request):
        pass

    def do_POST(self, request):
        pass

    def do_HEAD(self, request):
        pass


# 访问者模式一个缺点就是它严重依赖递归，如果数据结构嵌套层次太深可能会有问题，
# 有时候会超过Python的递归深度限制(参考 sys.getrecursionlimit() )。
# 在跟解析和编译相关的编程中使用访问者模式是非常常见的。
class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))

    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))

    def visit_Add(self, node):
        self.binop(node, 'ADD')

    def visit_Sub(self, node):
        self.binop(node, 'SUB')

    def visit_Mul(self, node):
        self.binop(node, 'MUL')

    def visit_Div(self, node):
        self.binop(node, 'DIV')

    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction,))

    def visit_Negate(self, node):
        self.unaryop(node, 'NEG')


s = StackCode()
print(s.generate_code(t4))