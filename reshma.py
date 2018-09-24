best_game = {
    'player':'blank',
    'game_type':'type',
    'level':'level_infinity',
    'played_by':'username',
    'game_state':True,
    }


while True:
    best_game['player'] = input("what is your name?")

    print(best_game)

    for key,value in best_game.items():
        print(f"{key}: {value}")

      
    #dice game
        import random

dice_roller = {
    'name':"Bob",
    'age':22,
    }

dice_rolls = []
    
for value in range (0, 17):
    dice_rolls.append(random.randint(1,7))


    print(dice_rolls)

    dice_rolls = 0
    
 while True:
     #a variable of user_inputs that stores the value from inout ()
    new_name = input ("what is your name? ")
    dice_roller['name'] = new_name
    new_age = input ("what is your age ?")
    dice_roller['age'] = new_age

    roll_command = inout("press enter to roll the dice!:")
    dice_roll = random.radint(1,7)
    print("you rooled a %s " % dice_roll)

    return True
dice_rolled

    

    
        

        


        

        
