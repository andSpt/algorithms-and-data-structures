import sys
from collections import deque


class MaxStack:
    def __init__(self):
        self.stack = deque()
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        return value

    def get_max(self):
        if not self.max_stack:
            return 0
        return self.max_stack[-1]

max_stack = MaxStack()

quantity = int(sys.stdin.readline())

for _ in range(quantity):
    data = sys.stdin.readline().split()
    if len(data) == 2:
        num = int(data[1])
        max_stack.push(num)
    elif data[0] == 'pop':
        max_stack.pop()
    elif data[0] == 'max':
        print(max_stack.get_max())


# import sys
# from collections import deque
#
# maximum = 0
#
# quantity = int(sys.stdin.readline())
# stack = deque()
#
# for _ in range(quantity):
#     data = tuple(sys.stdin.readline().split())
#     if len(data) == 2:
#         num = int(data[1])
#         stack.append(num)
#         if num > maximum:
#             maximum = num
#     else:
#         if data[0] == 'pop':
#             del_num = stack.pop()
#             if del_num == maximum:
#                 maximum = max(stack)
#         elif data[0] == 'max':
#             print(maximum)
