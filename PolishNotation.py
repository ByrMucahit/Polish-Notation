import operator

OPERATIONS = {'+': operator.add, '*': operator.mul, '-': operator.sub, '/': operator.floordiv}

# TRANSACTION OPERATIONS
def evaluate_rpn(expr):
    stack = [] # HOLDING CALCULATED NUMBER
    i = 0
    for el in expr:
        i += 1
        if el in OPERATIONS: # IF STACK GOT OPERATIONS SUCH AS '+','*' , THIS CONDITION İS APPLIED .
            operand2 = stack.pop() # NUMBERS IS POPPED UP TO CALCULATING
            operand1 = stack.pop()
            stack.append(OPERATIONS[el](operand1, operand2)) # ADDING NUMBER TO STACK AFTER CALCULATING 
        else: # IF NOT , THIS CONDITION APPLIED. THIS CONDITION MEANS THAT EXPR expression HAS NUMBER
            stack.append(el)
        print("{} . processing is {}".format(i,stack)) # CHECKING PROCESSING OUT AND DISPLAYING
    return stack.pop()


# TRANSACTION OPERATIONS 
# IN THIS SNIPPET'S PURPOSES IS PROCESSING THAT GIVEN INPUT. WE WANT TO USER INPUT .
# THEN THE GIVEN INPUT IS RAW. SO THAT WE CAN'T USE THIS INPUT WITH THIS WAY , WE NEED TO DO   DATA PROCESSING TO USING THAT'S WHY WE WILL USE FUNCTION BELOW .
def data_preprocessing(arr):
    reverse_arr = arr[::-1]
    splitted_array = reverse_arr.split()
    #ARRAY HAS BOTH INTEGER VARIABLES AND STRING VARIABLES. WE MUST SPLIT IT UP
    stack = []
    for i in range(0,len(splitted_array)):
        if splitted_array[i] == "+" or splitted_array[i] == "*": # IF THING OF WITHIN ARRAY IS OPERATOR , WE WON'T CHANGE. 
            stack.append(splitted_array[i])
        else : # IF IT IS NUMBER , WE NEED TO CONVERT TO INTEGER VALUE BECAUSE WE NEED TO DO TRANSACTION WITH THOSE VARIABLES 
            t = int(splitted_array[i])
            stack.append(t)
    return stack

def initaly():
    arr = []
    print("----------------------------WARNING--------------------------------------------------------------------")
    print("PLEASE, AFTER EACH PER CHRACTER ,  MAKE A BLANK AS MUCH AS ONE  CHARACTER MEASUREMENT ")
    arr = input('Please Entry Character: ')
    nArr = data_preprocessing(arr)


    print(arr)
    print("RESULT IS : {}".format(evaluate_rpn(nArr)))

initaly()