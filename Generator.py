import random as ra
import string 

# password ruls 
#    1- must at least by 9 ch 
#    2- it must have a least one punctuation and letter

class PassWordGenerator :
    
    # Easy password with Numbers only 
    def EasyPassword (self):
     password = ""
     for ch in range(9):
        password += str(ra.randint(0 , 9))
     return password

    # password with Nch and nubmers make it somewho difecalte
    def MidPassword(self):
       password = ""
       for ch in range(9):
        ch = ch * ra.randint(0 , 9)
        if ch%2 == 0 :
            password +=ra.choice(string.digits)
        else : 
            password +=ra.choice(string.ascii_letters)

       return password
    

  # password with Nch and nubmers and punctuation randmly  
    def HighLevelPassword(self):
        password = ""
        for _ in range(9):
           val = ra.randint(0, 72)
           if val % 2 == 0:
               password += ra.choice(string.digits)
           elif val % 3 == 0:
               password += ra.choice(string.ascii_letters)
           else:
               password += ra.choice(string.punctuation)

        if self.__cheakPasswordValid__(password):
           return password
        else:
           print("i am here ")
           random_index = ra.randint(0 , 8)
           if random_index == 0 :
              random_index_puc = ra.randint(1 ,random_index) 
           else :
                random_index_puc = ra.randint(0 ,random_index)
                          
           if random_index == random_index_puc and not 8 :
              random_index_puc +=1
           else :
              random_index_puc =0 

           print (random_index)
           print(random_index_puc)
           passwordAsList = list(password)
           passwordAsList[random_index] = ra.choice(string.ascii_letters)
           passwordAsList[random_index_puc] = ra.choice(string.punctuation)
           newPassword = "".join(passwordAsList)
           return newPassword

    
     # cheak if the password at least have one punctuation and one letter 
    def __cheakPasswordValid__(self , password):
        has_letter = False
        has_punc = False

        for ch in password :
          if ch.isalpha():
            has_letter =True
          elif ch in string.punctuation:
            has_punc = True 

        if has_letter and  has_punc :
           return True 
        
        return False     
                  
       
       
      
if __name__ == "__main__":
   NewPassword = PassWordGenerator()
   print(NewPassword.EasyPassword())
   print(NewPassword.MidPassword())
   print(NewPassword.HighLevelPassword())







     