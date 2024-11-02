a = 0

def escopo():
     global a
     a = 10

escopo()

print(a)
