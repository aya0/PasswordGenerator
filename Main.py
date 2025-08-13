import time 
from Generator import PassWordGenerator as passw
passwordObject =  passw()

Exit = False
print("welcome to Password Generator ")
while Exit == False :
    time.sleep(2)
    print("Choice the password you want ( please enter the number of the choice ) : ")
    time.sleep(1)
    print(" 1- Easy Password ")
    time.sleep(1)
    print(" 2- Mid Password ")
    time.sleep(1)
    print(" 3- secure password ")
    time.sleep(1)
    print(" 4- Exit ")

    choice = input()
    
    print (choice)
    if(int(choice) == 1 ):
       time.sleep(1)
       print(f" This is your password: "+ passwordObject.EasyPassword()) 
    elif(int(choice) == 2 ):
        time.sleep(1)
        print(f" This is your password: "+passwordObject.MidPassword())
    elif(int(choice) == 3 ):
        time.sleep(1)
        print(f" This is your password: "+passwordObject.HighLevelPassword())
    elif(choice == 4 ):
        Exit = True    
    else :
        time.sleep(1)
        print ("Please Enter a right Number for choice ")           


