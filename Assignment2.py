names = ['bruce', 'steven', 'tony', 'jerry', 'Anna', 'Nate']

'''
for n in names:
    print(n)
    print(len(n))


for n in names:
    if len(n) > 4:
        print(n)
        print(len(n))


for n in names:
    if len(n) > 5 and 'N' in n or 'n' in n:
        print(n)
        print(len(n))

'''
while len(names) >= 1:
    names.pop()
    print(names)