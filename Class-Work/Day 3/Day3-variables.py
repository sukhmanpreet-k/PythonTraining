x=30
print('global variable is',x)

def f1():
    a=20
    print('local variable used inside the f1 is',a)
f1()


def f2():
    print('\nprinting global variable inside the function')
    global x
    print(x)
f2()

print('nonlocal variables')
def f():
    b=40
    print('inside function \'f\' , local variable of \'f\' is ',b)
    def g():
        c=50
        print('inside function \'g\' which is nested inside function \'f\',local variable of \'g\' is  ',c)
        nonlocal b
        print('inside function \'g\' nonlocal variable is ',b)
        global x
        print('inside function \'g\' global variable is ',x)
    g()
f()