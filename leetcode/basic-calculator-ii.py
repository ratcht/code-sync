class Solution:
    def calculate(self, s: str) -> int:
        ops = ["+", "-", "/", "*"]
        stack = []

        current_num = ""
        operation = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                current_num += c
            if (not c.isdigit() and c != " ") or i == len(s) - 1:
                if operation == "+" or operation == "-":
                    stack.append(int(operation + current_num))
                    current_num = c
                elif operation == "*":
                    lhs = stack.pop()
                    stack.append(int(lhs) * int(current_num))
                elif operation == "/":
                    lhs = stack.pop()
                    stack.append(int(int(lhs) / int(current_num)))
                operation = c
                current_num = ""

        result = 0
        while stack:
            result += stack.pop()
        return result