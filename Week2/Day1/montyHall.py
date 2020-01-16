import random 

def organize_game():
    door_contents = [1, 0, 0]
    # pass

    random.shuffle(door_contents)

    for i in range (0, len(door_contents)):
        if door_contents[i] == 1:
            winning_door = i

    return door_contents, winning_door

def game_time():
    door_nums = [0, 1, 2]

    # runs the previously written function, to organize the game
    # wich pkuts the contents behind
    door_contents, winning_door = organize_game()

    # We need the contestant to make a choice
    door_chosen = random.choice(door_nums)

    # W e need the game show host to open another door
    # pass

    # the game show the host must open a door that does not have
    # the 10 million dollars
    # but the door that must lso not be the one that the contestant
    # picked


    # make a list of unavailable door number left over
    unavailable_doors = [door_chosen, winning_door]
    
    # using sets to find the door number left over
    #
    door_to_open = set(door_nums).difference(unavailable_doors)

    # we can use the pop() function 
    door_to_open = door_to_open.pop()

    oppened_door = door_nums[door_to_open]

    # declare the variable that tells us whether the the win wouls come from 
    # switching, or staying.
    switched_win = False
    stayed_win = False


    # we need to see if we win by switching or by staying.
    # First we simulate the switch.
    # we can't switch ti either the door we already chose, or the door aht's 
    # already opened.
    unavailable_doors = [door_chosen, door_to_open]
    switched_choice = set(door_nums).difference(unavailable_doors)



    switched_choice = switched_choice.pop()

    #use the index value we established from the switched-choice variable
    # TO FIND OUT THE CONTESTS OF THE DOOR  behind it.
    if door_contents[switched_choice] == 1:
        switched_win = True

    if door_contents[door_chosen] == 1:
        stayed_win = True


    return int(switched_win), int(stayed_win)


def monte_carlo(N):


    total_switched_wins = 0
    total_stayed_wins = 0


    switched_win = 0
    stayed_win = 0
    for gmae_num in range (0,N):

        switched_win, stayed_win = game_time()

        if switched_win == 1:
            total_switched_wins +=1

        if stayed_win == 1:
            total_stayed_wins +=1

    print(f"Out of {N} plays")
    print(f"Switched win percentage = { (total_switched_wins/N) * 100 } %")
    print(f"Stayed win percentage = { (total_stayed_wins/N) * 100 } %")



#game_time(100)
monte_carlo(1000000)



# list1 = [1,1,1,1,1,1,5,6,7]
#print(set(list1))


#list2 = [1,6,7]

#list3 = []

#list3 = set (list1).difference(list2)


# help(random.shuffle)