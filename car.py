import time
car_statis = "2"
on_or_off = {"1": "Started", "2": "Stopped,"}
program_stat = True
while program_stat:
    user_car = input("1 - Start \n2 - Stop \n3 - Exit \n")
    if user_car == "1" and car_statis is not "1":
        car_statis = "1"
        print("Starting Car")
        time.sleep(1)
        print("Vrrrrrr")
    elif user_car == "1" and car_statis is "1":
        print("car is already start")
        print("Try again")
    elif user_car == "2" and car_statis is not "2":
        car_statis = "2"
        print("Car comes to a full stop")
    elif user_car == "2" and car_statis is "2":
        print("Car is already started")
        print("Try again")
    elif user_car == "3":
        print("Thanks for comming")
        time.sleep(2)
        program_stat = False
    else:
        print("invalid input try again")        