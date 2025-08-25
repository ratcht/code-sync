class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substring = ""
                x = stack.pop()
                while x != "[":
                    substring = x + substring
                    x = stack.pop()

                k = 0
                i = 1
                while stack and stack[-1].isdigit():
                    x = stack.pop()
                    k += int(x) * i
                    i *= 10

                stack.extend(substring * k)
        
        return "".join(stack)