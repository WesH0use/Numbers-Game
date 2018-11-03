import random
#Import random library
winning_num = int(random.randint(1,10))

def guess_count():
    if guess_count == 1:
        print("That's it! Wow, you ARE a mind reader...That took you only 1 guess.")
    else:
        print("That's it! That took you {} guesses!".format(guess_counter + 1))

def start_game():
    print("Welcome. This is a simple number guessing game programmed using Python.\n")
    user_name = input("Let's start by choosing your user name:  \n")
    print("Let's see if you can read my mind",user_name + ".","Numbers are infinite, but I'll give you a range in which to guess.\n")
    print("When you're correct, I'll let you know how many attempts it took you to get it right.\n")   
    print("Alright {}, let's play.".format(user_name))
    
    
if __name__ == '__main__':
    start_game()

user_guess = 0    
guess_counter = 0 

while user_guess != winning_num:
    
    try:
        user_guess = (int(input("Pick a number betweewn 1 and 10   ")))
    except ValueError:
        guess_counter+=1
        print("That's not a valid number. Please try again... ")
        
    if user_guess > 10 or user_guess < 1:
        print("The range for selection is between 1 and 10.   ")
        print("\n Try another number!   ")
        guess_counter+=1
        continue 
        
    if user_guess > winning_num:
        print("The number is LOWER. Try again... ")
        guess_counter+=1
        continue
    if user_guess < winning_num:
        print("The number is HIGHER. Try again...  ")
        guess_counter+=1
        continue 
        
    

    break 

guess_count()