x =int(input('Enter the square root:'))
g =int(input('Enter guess:'))

if(x<0):
    print('error nagtive',x)
elif(x==0):
        print('error theres no square root for zero ')
else:
    
    
    while(g*g!=x):
            g=(g+x/g)/2
            if(g*g==x):
                print(g)
                break
     


