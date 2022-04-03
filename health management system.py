#health management system
#total - 6 files, 3 for food 3 for  workout
#3 clients avin wilwin nithi

def getdate():
    import datetime
    return datetime.datetime.now()

def log():
    print("which client do you want to log?")
    print("1. Avin")
    print("2.Wilwin")
    print("3.Nithi")
    print("Enter= " , end="")
    client_log=int(input())

    if client_log==1:
        print("What do you want to log for Avin?")
        print("1.Food")
        print("2.Workout")
        print("Enter = ",end="")
        log_no=int(input())
        if log_no==1:
            print("Enter food name= ",end="")
            with open("Avin-food.txt", "a") as avin_file:
                avin_file.write('[' + str(getdate()) + ']' + " " + input() + "\n")
        elif log_no==2:
            print("Enter workout name= ", end="")
            with open("Avin-workout.txt", "a") as avin_file:
                avin_file.write('[' + str(getdate()) + ']' + " " + input() + "\n")

    elif client_log==2:
        print("What do you want to log for Wilwin?")
        print("1.Food")
        print("2.Workout")
        print("Enter = ", end="")
        log_no = int(input())
        if log_no == 1:
            print("Enter food name= ", end="")
            with open("wilwin-food.txt", "a") as wilwin_file:
                wilwin_file.write('[' + str(getdate()) + ']' + " " + input() + "\n")
        elif log_no == 2:
            print("Enter workout name= ", end="")
            with open("wilwin-workout.txt", "a") as wilwin_file:
                wilwin_file.write('[' + str(getdate()) + ']' + " " + input() + "\n")

    elif client_log == 3:
        print("What do you want to log for Nithi?")
        print("1.Food")
        print("2.Workout")
        print("Enter = ", end="")
        log_no = int(input())
        if log_no == 1:
            print("Enter food name= ", end="")
            with open("nithi-food.txt", "a") as nithi_file:
                nithi_file.write('[' + str(getdate()) + ']' + " " + input() + "\n")
        elif log_no == 2:
            print("Enter workout name= ", end="")
            with open("nithi-workout.txt", "a") as nithi_file:
                nithi_file.write('[' + str(getdate()) + ']' + " " + input() + "\n")

    else:
        print("Pleasee check the input")
        print("Please enter the correct values")

def retrieve():
    print("which client do you want to Retrieve?")
    print("1. Avin")
    print("2.Wilwin")
    print("3.Nithi")
    print("Enter= ", end="")
    client_retrieve = int(input())

    if client_retrieve==1:
        print("What do you want to retieve for client Avin")
        print("1.Food")
        print("2.Workout")
        print("Enter= ",end="")
        retrieve_no=int(input())
        if retrieve_no==1:
            with open("avin-food.txt")as avin_file:
                print(avin_file.read())
        elif retrieve_no==2:
            with open("avin-workout.txt")as avin_file:
                print(avin_file.read())
        else:
            print("Please check your input")

    elif client_retrieve==2:
        print("What do you want to retieve for client Wilwin")
        print("1.Food")
        print("2.Workout")
        print("Enter= ",end="")
        retrieve_no=int(input())
        if retrieve_no==1:
            with open("wilwin-food.txt")as wilwin_file:
                print(wilwin_file.read())
        elif retrieve_no==2:
            with open("wilwin-workout.txt")as wilwin_file:
                print(wilwin_file.read())
        else:
            print("Please check your input")

    if client_retrieve==3:
        print("What do you want to retieve for client Nithi?")
        print("1.Food")
        print("2.Workout")
        print("Enter= ",end="")
        retrieve_no=int(input())
        if retrieve_no==1:
            with open("nithi-food.txt")as nithi_file:
                print(nithi_file.read())
        elif retrieve_no==2:
            with open("nithi-workout.txt")as nithi_file:
                print(nithi_file.read())
        else:
            print("Please check your input")

print("Welcome to Health Management System")
print("What do you want to do?")
print("1.LOG")
print("2.RETRIEVE")
print("Selelct Your Option= ",end="")
option=int(input())
if option==1:
    log()
elif option==2:
    retrieve()
else:
    print("please check your input")
