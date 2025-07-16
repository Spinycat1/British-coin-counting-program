#a software to count my coins. how I intend for it to work is the software will
#ask the user to input how much of each coin there are, then output the total in pounds and pence.

def counter_system(coin_value, coin_name):
    quantity_in = int(input(f"Please enter number of {coin_name}: "))
    carrier_var = (quantity_in * coin_value)
    return carrier_var

running = True #to ensure the program will be able to loop
while running == True: #checks the state of the program. e.g if the program is running, it will loop. else it will terminate.
    total = 0
    #below will count the pence coins
    total = total + counter_system(1, "1 pence coins")
    total = total + counter_system(2, "2 pence coins")
    total = total + counter_system(5, "5 pence coins")
    total = total + counter_system(10, "10 pence coins")
    total = total + counter_system(20, "20 pence coins")
    total = total + counter_system(50, "50 pence coins")

    #below will count pound coins and notes
    total = total + counter_system(100, "1 pound coins")
    total = total + counter_system(200, "2 pound coins")
    total = total + counter_system(500, "5 pound notes")
    total = total + counter_system(1000, "10 pound notes")
    total = total + counter_system(2000, "20 pound notes")
    total = total + counter_system(5000, "50 pound notes")

    #displays the total in pence and pounds
    print(f"You have {total}p or £{total / 100}")
    #asks if the user would like to count more, else will end the program by setting running to false.
    continue_inquiry = input("Would you like to calculate more?: ")
    if continue_inquiry == "Yes" or continue_inquiry == "Y" or continue_inquiry == "yes" or continue_inquiry == "y":
        running = True
    else:
        running = False
