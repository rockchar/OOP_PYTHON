'''
Generators are used to create iterators, but with a different approach. 
Generators are simple functions which return an iterable set of items, one at a time, in a special way.
When an iteration over a set of item starts using the for statement, the generator is run. 
Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, 
returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants, 
yielding each one in its turn.
'''

# let us write a function that generates the fibonacchi series

def fibonacchi(numberrange):
    a = 1
    b = 1
    for x in range(numberrange):
        yield(a)
        a,b = b, a+b


print(list(fibonacchi(10)))

fib = fibonacchi(10)

# wecan iterate through the functions using next

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
