#importing the time module
import time

#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

#wait for 1 second
time.sleep(1)

print ("Start guessing...")
#wait for 05sec
time.sleep(0.5)

#here we set the word synchronise. 
word = ("synchronise")

#creates an variable with an empty value
guesses = ''
turns = 10

#create a while loop
while turns > 0:         

    failed = 0             
    
    for char in word:      

        if char in guesses:    
    
        # print then out the character
            print (char,end=""),    

        else:
    
        # if not found, print a dash
            print ("_",end=""),     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    if failed == 0: 
        #print you won       
        print (" You won ")
    # exit the script
        exit()            
    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the synchronise  word
    if guess not in word:  
 
     # turns counter decreases with 1 
        turns -= 1        
 
    # print wrong
        print ("Wrong")  
 
    # how many turns are left
        print ("You have", + turns, 'more guesses' )
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose"  )