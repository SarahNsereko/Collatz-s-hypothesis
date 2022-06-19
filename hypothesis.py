check_loop =False

c0= int (input ("Enter any non negative number or non zero number "))
while c0 <=0:
    c0=input("Enter a non negative or non zero digit")
    if c0>0:
        break
   

   

while check_loop ==False :
    print (c0)
    if c0 %2==0:
        c0 = c0/2
        print(c0)
    else:
        c0 = (3*c0)+1
        print(c0)
       
    if c0 == 1:
        check_loop = True
        print(c0)
       
       