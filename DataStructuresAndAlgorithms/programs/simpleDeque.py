
from collections import deque

# if you are not aware about the size of deque
deque_op = deque(maxlen=3)
deque_op.append(1)
deque_op.append(2)
deque_op.append(3)
deque_op.append(4)
deque_op.append(5)
deque_op.append(6)

print(deque_op)

deque_op.pop()
print(deque_op)

deque_op.popleft()
print(deque_op)




