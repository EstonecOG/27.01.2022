memory = []

def lists():
    return 'lists'

def python():
    print('python')
    memory.append(lists)
    return lists

access = python

print(access()().upper())
print(memory)
print(memory.pop()().upper())
