if 1 == 0:
    print("hello")
else:
    print("world")

try:
    1 / 0
except ZeroDivisionError:
    print("hello")
else:
    print("world")

for i in range(10):
    print(i)
else:
    print("for-else")

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while-else")
