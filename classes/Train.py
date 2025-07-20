from .Carriage import Carriage

class Train:
    def __init__(self, carriage: Carriage = None):
        self.head = carriage
    
    def print(self):
        ''' prints the conteants of the linked list in an ascii train '''

        # initialize lines of train ascii art
        line1 = "\n    o x o x o x o . . .   "
        line2 =   "   o      _____           "
        line3 =   " .][__n_n_|DD[  ====_____ "
        line4 =   ">(________|__|_[_________]"
        line5 =   "_/oo OOOOO oo`  ooo   ooo "

        # places each line of the train's drawing space into an array
        drawSpace = [line1, line2, line3, line4, line5]

        # skips drawing head node
        current = self.head

        # draw each carriage's data inside of a ascii art carriage
        while (current != None):
            # print the current carriage
            current.print(drawSpace)

            # increment pointer
            current = current.next

        # print all lines of train ascii art
        print(drawSpace[0])
        print(drawSpace[1])
        print(drawSpace[2])
        print(drawSpace[3])
        print(drawSpace[4])

    
    def add(self, data):
        ''' adds a new node to end of list containing input data '''

        # if the head of the list is empty
        if (self.head == None):
            self.head = Carriage(data)
            return

        current = self.head

        # set current node to tail node of linked list
        while (current.next != None):
            current = current.next

        # add new node
        current.next = Carriage(data)


    def removeData(self, data):
        ''' 
        removes the first instance of some input data from an input linked list     
        returns 1 for success and 0 for failiure
        '''

        # if the list is empty
        if (self.head == None):
            print(" no data to remove!\n")
            return 0

        # if data is in first node
        if (self.head.data == data):
            self.head = self.head.next
            return 1

        # initialise pointers
        prevNode = self.head
        currentNode = self.head.next

        # find node with next node containing data equal to input data
        while (currentNode != None and currentNode.data != data):
            # increment both pointers
            currentNode = currentNode.next
            prevNode = prevNode.next
        
        # handle data not found
            if (currentNode == None):
                print("\n data not found in list\n")
                return 0
        
        # cut out data containing node
        prevNode.next = currentNode.next

        return 1
    

    def removeIndex(self, index):
        '''
        removes node at an input index 
        returns 1 for success and 0 for failiure
        '''

        # handle empty list
        if (self.head == None):
            print("\n train already empty! \n")
            return 0

        # handle index 0
        if (index == 0):
            self.head = self.head.next
            return 1

        # handle negative index
        if (index < 0):
            print("\n index out of range! \n")
            return 0

        prevNode = self.head
        currentNode = self.head.next
        currentIndex = 1

        # sets currentNode to node previous to input index
        while (currentIndex <= index and currentNode != None):
            currentNode = currentNode.next
            prevNode = prevNode.next
            currentIndex += 1

        # if index is out of range (null node reached)
        if (currentNode == None):
            print("\n index out of range! \n")
            return 0

        # cut out selected node
        prevNode.next = currentNode.next

        return 1

    
    def reverseList(self):
        ''' reverses an input linked list '''

        # list is empty
        if (self.head == None):
            return 
        
        # initialise pointers
        prev = None
        curr = self.head

        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev



    
    def clear(self):
        ''' clears all carriages '''

        # handle empty train
        if (self.head == None):
            return
        
        # let garbage collection take care of all carriage objects
        self.head = None