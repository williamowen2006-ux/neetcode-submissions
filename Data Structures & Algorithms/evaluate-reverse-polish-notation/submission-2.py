class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens: 
            if n.lstrip('-').isdigit(): 
                stack.append(int(n))
            else: 
                b = stack.pop()
                a = stack.pop() 
                if n == "+":
                    stack.append(a + b)
                elif n == "-":
                    stack.append(a - b)
                elif n == "*":
                    stack.append(a * b)
                elif n == "/":
                    if b == 0:
                        return 0
                    stack.append(int(a / b)) 
        return stack.pop()