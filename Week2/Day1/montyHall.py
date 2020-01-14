import random 

def organize_game():
    door_contents = [1, 0, 0]
    pass

    random.shuffle(door_contents)

    for i in range (0, len(door_contents)):
        if door_contents[i] == 1:
            winning_door = i

    return door_contents, winning_door

def game_time():
    door_nums = [0, 1, 2]

    door_contents, winning_choice = organize_game()

    # We need the contestant to make a choice
    door_chosen = random.choice(door_nums)

    # W e need the game show host to open another door
    # pass

    # the game show the host must open a door that does not have
    # the 10 million dollars
    # but the door that must lso not be the one that the contestant
    # picked

    unavailable_doors = [door_chosen, winning_door]
    door_to_open = set(door(door_nums).difference(unavailable_doors))
    door_to_open = door_to_open.pop()

    # Use if the 
    swiched_win = False
    stayed_win = False




# list1 = [1,1,1,1,1,1,5,6,7]
#print(set(list1))


#list2 = [1,6,7]

#list3 = []

#list3 = set (list1).difference(list2)


# help(random.shuffle)