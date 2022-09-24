from sympy import simplify
myexpr = input('Please input your expression: ')
ans = str(simplify(myexpr))
print(myexpr + ' = ' + ans)