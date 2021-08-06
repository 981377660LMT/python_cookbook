# ast 模块能被用来将Python源码编译成一个可被分析的抽象语法树（AST）
import ast

ex = ast.parse('2 + 3*4 + x', mode='eval')
print(ast.dump(ex))

# 分析这些节点最简单的方法就是定义一个访问者类
# 实现很多 visit_NodeName() 方法， NodeName() 匹配那些你感兴趣的节点
class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)


# Sample usage
if __name__ == '__main__':
    # Some Python code
    code = '''
for i in range(10):
    print(i)
del i
    '''

    # Parse into an AST
    top = ast.parse(code, mode='exec')

    # Feed the AST to analyze name usage
    c = CodeAnalyzer()
    c.visit(top)
    print('Loaded:', c.loaded)
    print('Stored:', c.stored)
    print('Deleted:', c.deleted)

    # AST可以通过 compile() 函数来编译并执行
    exec(compile(top, '<stdin>', 'exec'))

