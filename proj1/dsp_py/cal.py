string = input(r'Please input your expression: ')
a, op, b = string.split(' ')
x = [a, b]
X = [[], []]
for i in range(2):
    num = x[i]
    if '/' in num:
        index = num.index('/')
        X[i] = [int(num[:index]), int(num[index + 1:])]
    else:
        X[i] = [int(num), 1]

if op == '+':
    ans = [X[0][0]*X[1][1] + X[1][0]*X[0][1], X[0][1]*X[1][1]]
elif op == '-':
    ans = [X[0][0]*X[1][1] - X[1][0]*X[0][1], X[0][1]*X[1][1]]
elif op == '*':
    ans = [X[0][0]*X[1][0], X[0][1]*X[1][1]]
elif op == '/':
    ans = [X[0][0]*X[1][1], X[0][1]*X[1][0]]

for i in range(2,max(ans)):
    while((ans[0]%i == 0) and (ans[1]%i == 0)):
        ans[0] //= i
        ans[1] //= i

print(string + ' = ' + str(ans[0]) + '/' + str(ans[1]))

