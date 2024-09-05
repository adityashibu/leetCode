class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        
        if x > y:
            for char in s:
                stack.append(char)
                
                while len(stack) >= 2:
                    if stack[-2] == "b" and stack[-1] == "a":
                        stack.pop()
                        stack.pop()
                        
                        score += x
                    else:
                        break
                        
        else:
            for char in s:
                stack.append(char)
                
                while len(stack) >= 2:
                    if stack[-2] == "b" and stack[-1] == "a":
                        stack.pop()
                        stack.pop()
                        
                        score += y
                    else:
                        break
                        
                        
        stack2 = []
        for char in stack:
            stack2.append(char)
            
            while len(stack) >= 2:
                if stack2[-2] == "b" and stack[-1] == "a":
                        stack2.pop()
                        stack2.pop()
                        
                        score += x
                elif stack2[-2] == "b" and stack[-1] == "a":
                        stack2.pop()
                        stack2.pop()
                        
                        score += y
                else:
                    break
                
            
        return score