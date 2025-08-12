import math as ma
import random as ra

# password ruls 
#    1- must at least by 9 ch 
#    2- it must have a least one spechial ch

class PassWordGenerator :
    
    # Easy password with Numbers only 
    def EasyPassword ():
     password = ""
     for ch in range(9):
        password += str(ra.randint(0 , 9))
     return password

    # password with 







     