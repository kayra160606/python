print('1. Area of circle')
print('2. Area of triangle')
print('3. Area of square and rectangle')
print('4. Find simple Interest')
print('5. Exit')
ch=int(input('Enter your choice :'))
while(ch!=5):
    
    if(ch==1):
        r=int(input('Enter value of r :'))
        ans=3.14*r*r
        print('Area of circle is :',ans)
    
    elif(ch==2):
        l=int(input('Enter value of l :'))
        h=int(input('Enter value of h :'))
        t=1/2*l*h
        print('Area of triangle is :',t)
    
    elif(ch==3):
        side=int(input('Enter side length of square :'))
        area_squ=side * side
        print('Area of square is :',area_squ)
        w=float(input('Please enter the width :'))
        h=float(input('Please enter the height :'))
        area= w * h
        print('Area of square is :',area)
    
    elif(ch==4):
        p=int(input('Enter P :'))
        r=int(input('Enter R :'))
        n=int(input('Enter N :'))
        i=(p*r*n)/100
        print('simple interest :',i)
    
    elif(ch==5):
        exit()
    
    
    else:
        print('Invalid choice darling... ')
    
    
    print('1. Area of circle')
    print('2. Area of triangle')
    print('3. Area of square and rectangle')
    print('4. Find simple Interest')
    print('5. Exit')

    ch=int(input('Enter your choice :'))