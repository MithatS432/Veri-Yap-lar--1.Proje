# 1. ADT: Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):   # O(1)
        self.items.append(item)

    def pop(self):          # O(1)
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):         # O(1)
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):     # O(1)
        return len(self.items) == 0


# 2. Kullanım: Parantez dengeleme kontrolü
def is_balanced(expr):
    stack = Stack()
    for char in expr:                      # O(n)
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            top = stack.pop()
            if not top or not matches(top, char):
                return False
    return stack.is_empty()

def matches(opening, closing):
    pairs = { '(': ')', '[': ']', '{': '}' }
    return pairs.get(opening) == closing


# 3. Test
print(is_balanced("([{}])"))   # True
print(is_balanced("((())"))    # False
