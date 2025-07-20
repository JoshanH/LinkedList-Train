MAX_DATA_LEN = 16
CARRAGE_LEN = 18

class Carriage:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def print(self, drawSpace):
        text = str(self.data)[:MAX_DATA_LEN]
        textLen = len(text)

        # check if odd length
        if (textLen % 2 == 1):
            # make length even with whitespace
            text += " "

        # calculates amount of white space to add to either side of the data text
        buffSpc = (CARRAGE_LEN - textLen)//2

        drawSpace[0] +=  " ,_____=======_||____"
        drawSpace[1] +=  " |               -> |"
        # ensure whitespace is correctly formatted for data cont line
        drawSpace[2] +=  " |" + (" " *  buffSpc) + text + (" " * buffSpc) + "|"
        drawSpace[3] +=  "_|__________________|"
        drawSpace[4] +=  "  'o!o          o!o` "