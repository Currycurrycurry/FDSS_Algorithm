class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name = list(name)
        typed = list(typed)
        while name:
            c = name.pop()
            if not typed or typed.pop() != c:
                return False
            if not name or name[-1] != c:
                while typed and typed[-1] == c:
                    typed.pop()
        return not typed


import re
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        return re.match('^' + re.sub(r'((\w)\2*)', r'\1+', name) + '$', typed) is not None


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_index, typed_index = 0, 0
        while typed_index < len(typed):
            if name_index < len(name) and name[name_index] == typed[typed_index]:
                name_index += 1
                typed_index += 1
            elif typed_index > 0 and typed[typed_index] == typed[typed_index-1]:
                typed_index += 1
            else:
                return False
        return name_index == len(name)