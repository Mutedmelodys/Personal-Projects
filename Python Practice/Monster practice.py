"""
def userDefFunction (arg1, arg2, arg3 ...):
    program statement1
    program statement3
    program statement3
    ....
   return;
"""
 
def square(x):
    y = x * x
    return y

def sum_of_squares( x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a + b + c

a = input("what is the a number: ")
b = input("what is the b number: ")
c = input("what is the c number: ")

result = sum_of_squares(a, b, c)
print(result)
