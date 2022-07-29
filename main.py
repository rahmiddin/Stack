class Stack:

    def __init__(self):
        self.stack = []

    def isempty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return 'Empty'
        else:
            self.stack.pop()
            return self.stack[-1]

    def peek(self):
        if len(self.stack) == 0:
            return 'empty'
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


close_list = ["]", "}", ")"]


# Function to check parentheses
def check(myStr):

    stack_str = Stack()
    staples = []
    
    for item in myStr:
        stack_str.push(item)
    
    len_stack = len(stack_str.stack)
    
    if len(stack_str.stack) % 2 != 0:
        return 'Unbalanced'
    else:
        for item in stack_str.stack[len_stack // 2:]:
            if item == "]":
                staples.append('[')
            elif item == '}':
                staples.append('{')
            else:
                staples.append('(')
                
    if list(reversed(staples)) == stack_str.stack[:len_stack // 2]:
        return 'Balanced'
    else:
        return 'Unbalanced'
        
    
    
    
    

print(check('(((([{}]))))'))