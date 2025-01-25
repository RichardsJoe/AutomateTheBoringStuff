def collatz(number):
    #number is even
    if number % 2  == 0:        
        number = number//2
        print(number)
        return number
    #number is odd
    else:
        number = 3*number +1
        print(number)
        return number
    
# get user input
while True:
    try:
        number = input("Enter a number: ")
        number = int(number)
        break
    # verify user input
    except ValueError:
        if number is str:
            print("Please enter a valid number.")
    
while number != 1:
    number = collatz(number)