__author__  = 'Chilufya Mukuka'

import time

#this section build equations from user input

user_data = input('Enter the x, y and solution, seperated spaces(eqn1): ')

raw_eqn = user_data.split(' ')

eqn = raw_eqn[0] + 'x' + ' + ' + raw_eqn[1] + 'y' + ' = ' + raw_eqn[2]


user_data = input('Enter the x, y and solution, seperated spaces(eqn2): ')

raw_eqn2 = user_data.split(' ')

eqn2 = raw_eqn2[0] + 'x' + ' + ' + raw_eqn2[1] + 'y' + ' = ' + raw_eqn2[2]

print(eqn)
print(eqn2)
'''
print(eqn)
print(eqn2)
'''
'''
    [2x + 2y = 3]
    [3x + 4y = 7]


    3|[2x + 2y = 3]
    2|[3x + 4y = 7]
  -----------------
    |

'''

# type casting to interger form for calculations
int_raw_eqn = []

for item in raw_eqn:
    i = int(item)
    int_raw_eqn.append(i)


#print(int_raw_eqn)

int_raw_eqn2 = []

for item in raw_eqn2:
    i = int(item)
    int_raw_eqn2.append(i)


#print(int_raw_eqn2)



#elimination method
print('='*30)
mult_int_raw_eqn = []

for x in range(3):
    
    mult_int_raw_eqn.append(int_raw_eqn[x]*int_raw_eqn2[0])

#print(mult_int_raw_eqn)

mult_int_raw_eqn2 = []

for x in range(3):
    
    mult_int_raw_eqn2.append(int_raw_eqn2[x]*int_raw_eqn[0])

print(mult_int_raw_eqn2)
print(' After multiplying, we have : ')

print(str(mult_int_raw_eqn[0]) + 'x + ' + str(mult_int_raw_eqn[1]) + 'y = ' + str(mult_int_raw_eqn[2]))
print(str(mult_int_raw_eqn2[0]) + 'x + ' + str(mult_int_raw_eqn2[1]) + 'y = ' + str(mult_int_raw_eqn2[2]))

#subtracting to one common equation

final_eqn = []
final_eqn.append(mult_int_raw_eqn[0] - mult_int_raw_eqn2[0])
final_eqn.append(mult_int_raw_eqn[1] - mult_int_raw_eqn2[1])
final_eqn.append(mult_int_raw_eqn[2] - mult_int_raw_eqn2[2])
print('='*30)

#print(final_eqn)


print(str(final_eqn[0]) + 'x + ' + str(final_eqn[1]) + 'y = ' + str(final_eqn[2]))

print('='*30)
# solving for y

y = final_eqn[2] / final_eqn[1]

x = (int_raw_eqn[2] - (int_raw_eqn[1]*y)) / int_raw_eqn[0]

print('x =  ' + str(x)[:5] + ' & y = ' + str(y)[:5])
