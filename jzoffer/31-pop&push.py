def validateStackSequences(pushed, popped):
    if len(pushed) != len(popped):
        return False
    push_i = 0
    pop_i = 0
    stack = []
    while push_i < len(pushed):
        if pushed[push_i] != popped[pop_i]:
            stack.append(pushed[push_i])
            push_i += 1
        else:
            stack.append(pushed[push_i])
            push_i += 1
            pop_i += 1
            stack.pop()
            while stack and stack[-1] == popped[pop_i]:
                stack.pop()
                pop_i += 1
    while pop_i < len(popped):
        if popped[pop_i] == stack[-1]:
            pop_i += 1
            stack.pop()
        else:
            return False
    return len(stack) == 0