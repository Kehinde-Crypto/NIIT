# let the user input the username and password
# then allow the user to input his username five times then after the password ans username then deny the users access



import sys
user_name = str(input("Enter the user_name: "))
pass_word = str(input("Enter the pass_word: "))



pass_word  = 12
for user_name in range(4):
       if user_name == 3:
           print("Access denied")
       elif user_name == 2:
             print("Access denied")
       else:
             print(user_name)
             if pass_word == 12:
                   print("valid details")
             else:
                   #print('Invalid details')
                    print(pass_word)
      
    

    



