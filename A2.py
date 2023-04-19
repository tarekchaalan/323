#Group names     : Tarek Chaalan, Nick Haga and Zhengyao Huang
#Assignment      : No.2
#Due date        : Thursday February 9, 2023

def evaluate_postfix(expression):
    stack = []
    variables = {}
    
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        elif token.isalpha():
            if token not in variables:
                value = int(input("Enter the value of " + token + ": "))
                variables[token] = value
            stack.append(variables[token])
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.append(result)
    
    return stack[0]

continue_evaluating = 'y'
while continue_evaluating.lower() == 'y':
    expression = input("Enter a postfix expression with a $ at the end: ")
    result = evaluate_postfix(expression[:-1])
    print("Expression's value is", result)
    continue_evaluating = input("CONTINUE(y/n)? ")
    print()