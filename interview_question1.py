n = int(input('Input number : '))
for i in range(n):
    for space in range(n-i-1):
        print(' ',end='')
    for star in range(i+1):    
        print('* ',end='')
    print('\n',end='') 