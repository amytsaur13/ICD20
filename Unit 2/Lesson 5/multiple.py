print("="*10)
print("Hello"*4)
print("-"*45)

def simple_function():
    x = 7
    y = 8
    z = 9
    return x, y, z
   
print(simple_function())

a,b,c = simple_function

print(a)
print(b)
print(c)

#The program must have the exact amount of things or exactly one variable
q,r,s = simple_function()
print(q,r)

d = simple_function()

print(d*4)