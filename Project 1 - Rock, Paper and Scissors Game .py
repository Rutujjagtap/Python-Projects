#!/usr/bin/env python
# coding: utf-8

# # ROCK, PAPER AND SCISSORS GAME 

# **AUTHOR AND DEVELOPER:** Rutuj Jagtap
# 
# **DESCRIPTION :**  
# This Jupyter Notebook contains a Python implementation of the classic game **"Rock, Paper, Scissors"**. The game is a simple yet entertaining way to pass the time, pitting two players against each other in a battle of wits and luck.
# 
# The rules are straightforward:
# 
# **- Rock beats scissors**  
# **- Scissors beats paper**  
# **- Paper beats rock**  
# 
# In this implementation, the user can play against the computer. The user is prompted to input their choice, and the computer randomly selects its choice (rock, paper, or scissors). The program then determines the winner based on the rules mentioned above and displays the result.
# 
# This code serves as a fun and educational introduction to basic Python programming concepts such as conditional statements, loops, functions, and random number generation.
# 
# *Feel free to run the code and challenge yourself to see who reigns supreme in this classic game of strategy and chance!*

# In[1]:


#Assigning Counters for counting the result status
Win = 0
Lose = 0
Tie = 0


#Asking the player to choose between Rock, Paper and Scissors :
while True:     #------> The loop will be executed till the condition is True
    user = int(input(f"Enter a number to select an object (1-Rock 2-Paper 3-Scissors 0-End Game) :\nGame Status - Win:{Win} Lose:{Lose} Tie:{Tie}\n"))
    
    if user<0 or user>3:      #------> Raising an exception if user entered number is not valid  
        raise Exception("Enter a valid number")
        
    import random             #------> immporting random integer between 1,2 and 3 as computer's choice to play a match 
    
    compt = random.randint(1,3)
   

#Using if else condition to decide the winner :
    if user == 1:             
        if compt == 1:
            Tie += 1
            print('You selected Rock, Computer selected Rock: \nIts a Tie')
            print(' ')
        elif compt == 2:
            Lose += 1
            print('You selected Rock, Computer selected Paper: \nComputer Won!!!')
            print(' ')
        else:
            Win += 1
            print('You selected Rock, Computer selected Scissors: \nYou Won!!!')
            print(' ')
    
    if user == 2:
        if compt == 2:
            Tie += 1
            print('You selected Paper, Computer selected Paper: \nIts a Tie')
            print(' ')
        elif compt == 1:
            Win += 1
            print('You selected Paper, Computer selected Rock: \nYou Won!!!')
            print(' ')
        else:
            Lose += 1
            print('You selected Paper, Computer selected Scissors: \nComputer Won!!!')
            print(' ')
    
    if user == 3:
        if compt == 3:
            Tie += 1
            print('You selected Scissors, Computer selected Scissors: \nIts a Tie')
            print(' ')
        elif compt == 1:
            Win += 1
            print('You selected Scissors, Computer selected Rock: \nComputer Won!!!')
            print(' ')
        else:
            Lose += 1
            print('You selected Scissors, Computer selected Paper: \nYou Won!!!')
            print(' ')
            
    if user == 0:
        print(' ')
        print("----------Result----------")
        print(f"Won:{Win}     Lost:{Lose}     Tied:{Tie}")
        print("--------------------------")
        print("!!!Thank you for playing!!!")
        break
        


# ## 

# In[ ]:




