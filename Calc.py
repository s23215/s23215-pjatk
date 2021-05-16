def evaluate_plus(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a + b)

def evaluate_minus(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b - a)

def evaluate_multiply(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a * b)

def evaluate_divide(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b / a)

def evaluate_integer(expr, stack):
    stack.append(int(expr))

operators = {
    "+": evaluate_plus,
    "-": evaluate_minus,
    "": evaluate_multiply,
    "/": evaluate_divide,
    "p": lambda stack:print(stack[-1])
}

def evaluate_expression(expr, stack):
    for e in expr:
        try:
            evaluate_integer(e, stack)
        except ValueError:
            operators[e](stack)
    print(expr)
    pass

stack=[]

while True:
    expr=input()
    expr=expr.split()
    done=evaluate_expression(expr, stack)
    if done:
        break