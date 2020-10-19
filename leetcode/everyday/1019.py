class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1, stack2 = [], []
        for s in S:
            if s != '#':
                stack1.append(s)
            elif len(stack1):
                stack1.pop()
        for t in T:
            if t != '#':
                stack2.append(t)
            elif len(stack2):
                stack2.pop()
        stack1, stack2 = ''.join(stack1), ''.join(stack2)
        return stack1 == stack2
            
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(S):
            stack = []
            for s in S:
                if s != '#':
                    stack.append(s)
                elif len(stack):
                    stack.pop()
            return ''.join(stack)
        return helper(S) == helper(T)
