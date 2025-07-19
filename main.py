from classes.Carriage import Carriage
from classes.Train import Train

# input index constants
COMMAND_IND = 0
ARG_2_IND = 1
ARG_3_IND = 2

def handleInput(train: Train):
    ''' handles user input and draw CLI interface '''

    userInput = input("\nTrain>> ").split()

    # handles input command action (userInput[0] is user command)
    if (userInput[0] == "help"):
        print("\nCommand List: \n"
            "---------------------------------\n"
            "print \n"
            "add [data] \n"
            "remove data/index [data OR index] \n"
            "reverse \n"
            "clear \n"
            "exit \n")
        
        handleInput(train)
        
    elif (userInput[COMMAND_IND] == "add"):
        train.add(userInput[1])
        train.print()

    elif (userInput[COMMAND_IND] == "remove"):
        if (userInput[ARG_2_IND] == "data"):
            if (train.removeData(userInput[ARG_3_IND])):
                train.print()
            
        elif (userInput[ARG_2_IND] == "index"):
            if (train.removeIndex(int(userInput[ARG_3_IND]))):
                train.print()
        
        else:
            print("\n data or index removal not specified \n")

    elif (userInput[COMMAND_IND] == "reverse"):
        train.reverseList()
        train.print()
    
    elif (userInput[COMMAND_IND] == "print"):
        train.print()
    
    elif (userInput[COMMAND_IND] == "clear"):
        # let garbage collector delete all nodes of linked list
        train.clear()
        train.print()

    elif (userInput[COMMAND_IND] == "exit"):
        exit()

    else:
        print("\n please enter a valid command \n")

    handleInput(train)


# initialise liked list
train = Train()

# start taking input
handleInput(train)