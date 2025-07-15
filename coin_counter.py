#a software to count my coins. how I intend for it to work is the software will
#ask the user to input how much of each coin there are, then output the total in pounds and pence.

running = True #to ensure the program will be able to loop
while running == True: #checks the state of the program. e.g if the program is running, it will loop. else it will terminate.
    total = 0
    #below will count the pence coins
    one_pence_in = int(input("Please enter number of 1 pence coins: ")) 
    total = total + (one_pence_in * 1)
    two_pence_in = int(input("Please enter number of 2 pence coins: "))
    total = total + (two_pence_in * 2)
    five_pence_in = int(input("Please enter number of 5 pence coins: "))
    total = total + (five_pence_in * 5)
    ten_pence_in = int(input("Please enter number of 10 pence coins: "))
    total = total + (ten_pence_in * 10)
    twenty_pence_in = int(input("Please enter number of 20 pence coins: "))
    total = total + (twenty_pence_in * 20)
    fifty_pence_in = int(input("Please enter number of 50 pence coins: "))
    total = total + (fifty_pence_in * 50)
    #below will count pound coins and notes
    one_pound_in = int(input("Please enter number of 1 pound coins: "))
    total = total + (one_pound_in * 100)
    two_pound_in = int(input("Please enter number of 2 pound coins: "))
    total = total + (two_pound_in * 200)
    five_pound_in = int(input("Please enter number of 5 pound notes: "))
    total = total + (five_pound_in * 500)
    ten_pound_in = int(input("Please enter number of 10 pound notes: "))
    total = total + (ten_pound_in * 1000)
    twenty_pound_in = int(input("Please enter number of 20 pound notes: "))
    total = total + (twenty_pound_in * 2000)
    fifty_pound_in = int(input("Please enter number of 50 pound notes: "))
    total = total + (fifty_pound_in * 5000)
    #displays the total in pence and pounds
    print(f"You have {total}p or £{total / 100}")
    #asks if the user would like to count more, else will end the program by setting running to false.
    continue_inquiry = input("Would you like to calculate more?: ")
    if continue_inquiry == "Yes" or continue_inquiry == "Y" or continue_inquiry == "yes" or continue_inquiry == "y":
        running = True
    else:
        running = False
