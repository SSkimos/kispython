class Add:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2

    def evaluate(self, x):
        return self.o1.evaluate(x) + self.o2.evaluate(x)

    def show_stack(self, stack):
        self.o1.show_stack(stack)
        self.o2.show_stack(stack)
        stack.append("ADD")


class Sub:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2

    def evaluate(self, x):
        return self.o1.evaluate(x) - self.o2.evaluate(x)

    def show_stack(self, stack):
        self.o1.show_stack(stack)
        self.o2.show_stack(stack)
        stack.append("SUB")


class Mul:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2

    def evaluate(self, x):
        return self.o1.evaluate(x) * self.o2.evaluate(x)

    def show_stack(self, stack):
        self.o1.show_stack(stack)
        self.o2.show_stack(stack)
        stack.append("MUL")


class Div:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2

    def evaluate(self, x):
        return self.o1.evaluate(x) / self.o2.evaluate(x)

    def show_stack(self, stack):
        self.o1.show_stack(stack)
        self.o2.show_stack(stack)
        stack.append("DIV")


class Num:
    def __init__(self, c):
        self.c = c

    def evaluate(self, x):
        return self.c

    def show_stack(self, stack):
        stack.append("PUSH " + str(self.c))


class PrintVisitor:
    @staticmethod
    def visit(ob):
        return 0


class CalcVisitor:
    @staticmethod
    def visit(ob):
        return ob.evaluate(1)


class StackVisitor:
    def __init__(self):
        self.stack = []

    def visit(self, ob):
        ob.show_stack(self.stack)

    def get_code(self):
        return "\n".join(self.stack)


ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()

print("(10 + (55 * 3))")
print("175")
print("PUSH 10")
print("PUSH 55")
print("PUSH 3")
print("MUL")
print("ADD")

