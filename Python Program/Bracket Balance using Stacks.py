# Python3 program to check for
# balanced brackets.
 
# function to check if
# brackets are balanced
 
# function definition 
def demoOfStack(expr):
    stack = []
    # traversing the expression
    for char in expr:
        if char in ["(", "{", "["]:
            # pushing the element
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Checking whether the stack is Empty
    if stack:
        return False
    return True
if __name__ == "__main__":
    # getting the expression from the user
    expr = input()
    # Function call
    if demoOfStack(expr):
        print("Balanced")
    else:
        print("Not Balanced")
 