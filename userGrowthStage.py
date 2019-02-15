from datetime import datetime

currentYear = datetime.now().year

def userGrowthStage():
    try:
        yearOfBirth = int(input("Please Enter your Year Of Birth: "))

        if(yearOfBirth > currentYear):
            print("Please your Birth Year can not be more than the Current Year. \nHence Invalid!")
        elif(yearOfBirth < 0):
            print("Please you can not have a negative Birth Year. \nHence Invalid!")
        else:
            userAge = currentYear - yearOfBirth
            if(userAge < 18):
                print("User is minnor")
            elif(userAge >= 18 and userAge <= 36):
                print("User is youth")
            else:
                print("User is elder")
    except ValueError:
        print("Invalid Year Of Birth!")

userGrowthStage()
