class node:
    '''
    node object for linked list with a variable data type
    '''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def printTrain(head):
    ''' prints the conteants of the linked list in an ascii train '''

    # initilaise lines of train ascii art
    line1 = "    o o o o o o o . . .   "
    line2 = "   o      _____           "
    line3 = " .][__n_n_|DD[  ====_____ "
    line4 = ">(________|__|_[_________]"
    line5 = "_/oo OOOOO oo`  ooo   ooo "

    # skips drawing head node
    current = head.next

    # draw each node's data inside of a ascii art caridge
    while (current != None):
        line1 += " ____=======_||____"
        line2 += " |                 |"
        line3 += f" |  {str(current.data)[:5]}          |"
        line4 += "_|_________________|"
        line5 += " 'o!o         o!o`  "

        current = current.next

    # print all lines of train ascii art
    print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n")

    handleInput(head)


def addNode(head, data):
    ''' adds a new node to end of list containing input data '''

    current = head

    # set current node to tail node of linked list
    while (current.next != None):
        current = current.next

    # add new node
    current.next = node(data)

    printTrain(head)


def removeData(head, data):
    ''' 
    removes the first instance of some input data from an input linked list     
    '''

    # if the list is empty
    if (head.next == None):
        print(" no data to remove!\n")
        handleInput(head)

    # if data is in first node
    if (head.next.data == data):
        head = head.next
        printTrain(head)
        handleInput(head)

    prevNode = head
    currentNode = head.next

    # find node with next node containing data equal to input data
    while (currentNode.data != data):

        # handle data not found
        if (currentNode == None):
            print("\n data not found in list\n")
            handleInput(head)

        # increment both pointers
        currentNode = currentNode.next
        prevNode = prevNode.next
    
    # cut out data containing node
    prevNode.next = currentNode.next

    printTrain(head)


def removeIndex(head, index):
    ''' removes node at an input index '''

    # handle index 0
    if (index == 0):
        head = head.next
        printTrain(head)
        handleInput(head)

    # handle negative index
    if (index < 0):
        print("\n index out of range! \n")
        handleInput(head)

    prevNode = head
    currentNode = head.next
    currentIndex = 1

    # sets currentNode to node previous to input index
    while (currentIndex <= index and currentNode != None):
        currentNode = currentNode.next
        prevNode = prevNode.next
        currentIndex += 1

    # if index is out of range (null node reached)
    if (currentNode == None):
        print("\n index out of range! \n")
        handleInput(head)

    # cut out selected node
    prevNode.next = currentNode.next

    printTrain(head)


def reverseList(head):
    ''' reverses an input linked list '''

    # set initial pointers 
    prev = head
    curr = head.next

    # handle first node
    if (curr != None):
        next = curr.next # store next node
        curr.next = None # nullify .next pointer
        # increment all pointers
        prev = curr
        curr = next
        next = next.next
    else:
        # list empty, no changes needed
        printTrain(head)

    # handle rest of list
    while (curr.next != None):
        curr.next = prev # reverse node .next pointer
        # increment all pointers
        prev = curr
        curr = next
        next = next.next
    
    # handle final node
    curr.next = prev
    head.next = curr


    printTrain(head)


def handleInput(head):
    ''' handles user input and draw CLI interface '''

    userInput = input("\nTrain>> ").split()

    # handles input command action (userInput[0] is user command)
    if (userInput[0] == "help"):
        print("\nCommand List: \n"
            "----------------------\n"
            "print \n"
            "add [data] \n"
            "remove data/index [data OR index] \n"
            "reverse \n"
            "exit \n")
        
        handleInput(head)
        
    elif (userInput[0] == "add"):
        addNode(head, userInput[1])

    elif (userInput[0] == "remove"):
        if (userInput[1] == "data"):
            removeData(head, userInput[2])

        elif (userInput[1] == "index"):
            removeIndex(head, int(userInput[2]))
        
        else:
            print("\n data or index removal not specified \n")
            handleInput(head)

    elif (userInput[0] == "reverse"):
        reverseList(head)
    
    elif (userInput[0] == "print"):
        printTrain(head)

    elif (userInput[0] == "exit"):
        exit()

    else:
        print("\n please enter a valid command \n")
        handleInput(head)


# MAIN 

# initialise head of linked list
head = node("head_node")

# start taking input
handleInput(head)