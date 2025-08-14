import time 
from Generator import PassWordGenerator as passw
import HelperMethod as HM
passwordObject =passw()

Exit = False
print("welcome to Password Generator ")

while Exit == False :
    HM.PrintPuse("Choice the password's Level you want ( please enter the number of the choice ) : " , 2)
    HM.PrintPuse(" 1- Easy Password " ,1)
    HM.PrintPuse(" 2- Mid Password " ,1)
    HM.PrintPuse(" 3- secure password " ,1)
    HM.PrintPuse(" 4- Exit " ,1)

    choice = input()
    
    if(choice == '1' ):
       HM.PrintPuse(f" This is your password: "+ passwordObject.EasyPassword() , 1) 
    elif(choice == '2' ):
        HM.PrintPuse(f" This is your password: "+passwordObject.MidPassword() ,1)
    elif(choice == '3' ):
        HM.PrintPuse(f" This is your password: "+passwordObject.HighLevelPassword() ,1)
    elif(choice == '4' ):
        Exit = True    
    else :
        HM.PrintPuse ("Please Enter a right Number for choice " ,1)           


