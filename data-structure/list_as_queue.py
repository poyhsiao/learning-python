from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
re = queue.popleft()
print re
print queue

re = queue.popleft()
print re
print queue