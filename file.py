w = 'hello'
list = [ [w[:s+1]] for s in range(len(w)) ]
print(list)