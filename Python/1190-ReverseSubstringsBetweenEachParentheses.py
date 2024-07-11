class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                # Collect all characters until the matching '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the '(' from the stack
                if stack:
                    stack.pop()
                # Push the reversed substring back into the stack
                stack.extend(temp)
            else:
                # Push current character to stack
                stack.append(char)
        
        # Join the stack to form the final string
        return ''.join(stack)