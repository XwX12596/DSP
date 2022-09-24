from fractions import Fraction
que = input('Please input your expression:')
Num1,sym,Num2=que.split(' ')
print(que + ' = ' + str(eval('Fraction(Num1)' + sym + 'Fraction(Num2)')))