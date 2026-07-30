class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack == []:
                    return False
                x = stack.pop()
                if x == '(' and c != ')':
                    return False
                elif x == '{' and c != '}':
                    return False
                elif x == '[' and c != ']':
                    return False
        return stack == []
