import math
print("welcome to the online banking applicaion")


#create an account 
def signup():
    global name
    global password
    global CurrentBalance 

    name = str(input("please create a user name: "))
    password = str(input("please put in your 6 digit pin: "))

    if len(password) == 6:
        password = password

    else:
        print("please enter a 6 digit pin")
        password2 = str(input("enter 6 digit pin again: "))

        if len(password2) != 6:
            print("error! please enter a 6 digit pin")
            signup()

        else: 
            password = password2 

    print("thanks for creating your account with us!")


#signup()


#passcode recvery
def forgetPassword():
    NewPassword = str(input("please enter your new 6 digit pin: "))
    if len(NewPassword) != 6:
        print("error! the pin should be 6 digit long. Please try again: ")
        forgetPassword()

    else:
        print("your new pin has been saved")
        NewPassword = password


#forgetPassword()

        
#deposits 
def depositInterest(p,r,t):
   # a(future amount ) = p (principle/current amount) * e ^ (rt) 
   # this is the formula to calculate compound interest
    
    p= float(p)
    r= float(r)
    t= float(t)
    rt = r*t
    e= math.exp(rt)

    a = p*e #investment amount that the user will get in the future 
    return a 
    

#print(depositInterest(1000, 0.048 , 4))
#initialamount = 1000 GBP
#interest rate = 4.8%
#time = 4 years 


def login():
    userName = str(input("enter your user name: "))
    userPasscode = str(input("enter your 6 digit pin: "))

    #check if userName and userPasscode is registred/ present in the database.
    if userName == name and userPasscode == password:
        print("welcome to your bank account" + " " + name )
        print("please choose from the drop down menu")
        menulist = ["1-deposit","2-withdraw","3-transfer","4-deposit interest rate","5-check balance","6-calculate compound interest"]
        for b in menulist:
            print(b)
        choose = int(input("please enter the number of your choice: "))

        d = 0 #deposits
        w = 0 #withdrawals
        cb = 0 #current balance 

        if choose == 1:
            d = int(input("enter the amount to be deposited: "))
            cb = d
            print("your current balance is" + " " + str(cb))

        elif choose == 2:
            w = int(input("enter the amount to be withdrawn: "))
            if w > cb:
                print("your current balance is not sufficient")
                login()
            else: 
                cb = d - w
            print("your current balance is" + " " + str(cb) + " " + "after withdrawing" + " " + str(w) )

        elif choose == 3:
            reciever = str(input("Please enter the 8 digit account number of reciever : "))
            if len(reciever) == 8:
                amount = int(input("please enter the amount of money for transfer : "))
                if amount > cb:
                  print("this transaction can't be made due to insufficient amount")
                  login()
                else:
                    cb = d - amount
                    print("the transaction of" + " " + str(amount) + " " + "is completed")

            else:
                print("the transaction can't be done due to wrong account number")
                login()


        elif choose == 4:
            if d > 30000:
                rate = 3
            elif d > 20000:
                rate = 2
            else:
                rate = 1.3
            print("your current deposit interest rate" + " " + str(rate) + "%") 

        
        elif choose == 5:
            print("your current balance is " + " " + str(cb))

        elif choose == 6:
            compoundList = ["1 - calculate CI based on your current balance", "2- calculate CI based on your deposit input"]
            for n in compoundList:
                print(n)

            userChoice = int(input("please enter your choice : "))
            if userChoice == 1:
                duration = str(input("Please indicate the duration for which you would like to deposit the money in years "))
                if d > 30000:
                    interestRate = 3/100 
                elif d > 20000:
                    interestRate = 2/100
                else:
                    interestRate = 1.3/100
                print("your current balance in" + " " + "duration" + " " + " years wil be" )
                print(depositInterest(cb, interestRate,duration))

            elif userChoice == 2:
                duration = str(input("Please indicate the duration for which you would like to deposit the money in years "))
                money = str(input("Please enter the amount of money you would want to invest "))
                money = int(money)

                if d > 30000:
                    interestRate = 3/100 
                elif d > 20000:
                    interestRate = 2/100
                else:
                    interestRate = 1.3/100
                print("your current balance in" + " " + "duration" + " " + " years wil be" )
                print(depositInterest(money, interestRate,duration))



    else:
        print("either username or pin is wrong")
        print("Sign up if you are not registered with us. Do you already have an account? ")

        list1 = ["1-yes", "2- no"]
        for i in list1:
            print(i)
        userInput = int(input("enter your choice: "))
        if userInput == 1:
            list2 = [ "1 - login re-attempt", "2 - forget pin/username"]
            for e in list2:
                print(e)
            userAnswer = str(input('please enter your choice: '))
            userAnswer = int(userAnswer)
            if userAnswer ==1:
             login()
            elif userAnswer ==2:
                forgetPassword()  
            else:
             print("error. please try again ") 
             login()



        elif userInput == 2:
            print("please create your account first")
            signup()

        exit()

def mainmenu():
    option1 = int(input("choose 1 to sign up and choose 2 to login in" ))
    if option1 ==1:
        signup()
    elif option1 ==2:
        login()
    else:
        print("option is not available")
        mainmenu()

def exit():
    answer = str(input("do you want to exit? Yes or No "))
    if answer == "Yes":
        login()
    elif answer == "No":
        print("thank you for using the app")
    else:
        print("invalid command")
        mainmenu()

mainmenu()
    
    






    










    


    


               

