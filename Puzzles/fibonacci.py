import sys
def fibonacci(limit):
    a = 1
    b = 1
    fibo = [1,1]
    if limit == 1:
        print(fibo[0])
        return 
    if limit == 2:
        print(fibo)
        return
    for n in range(0, limit-2):
        c = a + b
        fibo.append(c)
        a = b 
        b = c
    print(fibo)

def fibonacci_recursion(n):
  if n < 2:
    return n
  else:
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

fibo = fibonacci_recursion(int(sys.argv[1]))
for i in range(int(sys.argv[1])):
       print(fibonacci_recursion(i))

