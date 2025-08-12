import math as ma
import random as ra
import string 

# password ruls 
#    1- must at least by 9 ch 
#    2- it must have a least one spechial ch

class PassWordGenerator :
    
    # Easy password with Numbers only 
    def EasyPassword (self):
     password = ""
     for ch in range(9):
        password += str(ra.randint(0 , 9))
     return password

    # password with Nch and nubmers 
    def MidPassword(self):
       password = ""
       for ch in range(9):
        if ch%2 == 0 :
            password +=ra.choice(string.digits)
        else :    
            password +=ra.choice(string.ascii_letters)
       return password
      
if __name__ == "__main__":
   NewPassword = PassWordGenerator()
   print(NewPassword.EasyPassword())
   print(NewPassword.MidPassword())







     