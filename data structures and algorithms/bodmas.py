# Implementing BODMAS

def operation(operator, operands):
    if operator == '+':
        return operands[0] + operands[1]
    if operator == '-':
        return operands[0] - operands[1]
    if operator == '*':
        return operands[0] * operands[1]
    if operator == '/':
        return operands[0] / operands[1]
    if operator == '^':
        return operands[0] ** operands[1]
     # '!': fact(operands[0])

def bodmas(expression):
    from array_stack import Arraystack
    operator_stack = Arraystack()
    operand_stack = Arraystack()
    left = '({['
    right = ']})'
    for element in expression.split(' '):
        if element in left:
            count = 0
        elif element in right:
            op_list = [operand_stack.pop() for i in range(count)]
            val = 0
            for j in range(0, count//2, 2):
                val += operation(operator_stack.pop(), [op_list[j:j+2])
        elif element in ['+', '-', '*', '/', '^']:
            operator_stack.push(element)
        else:
            operand_stack.push(element)
            count += 1
