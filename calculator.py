from tkinter import *
import logging              #logging.INFO => nie wyświetla
                            #logging.DEBUG => wyświetla
logging.basicConfig(level = logging.DEBUG)

root = Tk()
root.title('Calculator')

# Background color
root.configure(bg='#333438')

input_ = Entry(root, width=10, borderwidth=5, font=('Arial 24'))
input_.grid(row=0, column=0, columnspan=5, padx=30, pady=30)


# Buttons
plus_button = Button(root, text='+ ', padx=30, pady=30, 
                     command=lambda: operations('+',input_array))
plus_button.grid(column=3, row=3)

substract_button = Button(root, text=' - ', padx=30, pady=30,command=lambda: operations('-',input_array))
substract_button.grid(column=3, row=2)

is_equal = Button(root, text='= ', padx=30.4, pady=30, command=lambda: calculate(input_array))
is_equal.grid(column=3, row=4)

zero_button = Button(root, text='0', padx=30, pady=30, command=lambda: numbers(0))
zero_button.grid(column=0, row=4)

clear_button = Button(root, text='C ', padx=30, pady=30, command=lambda: clear_input())
clear_button.grid(column=3, row=1)

mulitplay_button = Button(root, text='x', padx=30 , pady=30, command=lambda: operations('*',input_array))
mulitplay_button.grid(column=1 , row= 4)

divison_button = Button(root, text='/ ', padx=29 , pady=30, command=lambda: operations('/',input_array))
divison_button.grid(column=2, row = 4)


input_array = []

def is_float(value):
    try:
        float_value = float(value)
        return True
    except ValueError:
        return False

def numbers(number):
    current = input_.get()
    input_.insert(len(current) + 1, number)
    
def operations(operator: str, input_array):

    logging.debug(f'Array po klinknieciu plus lub minus{input_array}')

    current_number = input_.get()
    input_.delete(0, END)

    if is_float(current_number):
        input_array.append(current_number)
        input_array.append(operator)

        logging.debug(f"array {input_array}")
    else:
        logging.debug("Nieprawidłowa liczba.")
    
    return input_array



def find_all_of_multiplay_signs(input_array):
    #List with all the indexes of a * sign 
    all_signs = [i for i, element in enumerate(input_array) if '*' in element]

    for i in reversed(all_signs):  
        index = i
        try:
            result = int(input_array[index - 1]) * int(input_array[index + 1])
        except:
            result = float(input_array[index - 1]) * float(input_array[index + 1])

        #Calculate the multiplication
        input_array[index - 1:index + 2] = [str(result)]
    return input_array

def find_all_of_division_signs(input_array):
    #List with all the indexes of a / sign 
    all_signs = [i for i, element in enumerate(input_array) if '/' in element]

    for i in reversed(all_signs):  
        index = i
        try:
            result = int(input_array[index - 1]) / int(input_array[index + 1])
        except:
            result = float(input_array[index - 1]) / float(input_array[index + 1])
    
    #Calculate the disvision
        input_array[index - 1:index + 2] = [str(result)]
    return input_array



def calculate(input_array : list):
    logging.debug(f'{input_array}')
    if len(input_array) == 0:
        return None
    
    current_number = input_.get()
    input_array.append(current_number)

    while(len(input_array)>1):

        #Check for / signs
        if '/' in input_array:

            find_all_of_division_signs(input_array)

            #Return the output if are only two numbers for instance 10/5
            if len(input_array) == 1:
                 input_.delete(0, END)
                 input_.insert(0,str(input_array[0]))
                 clear_global_input_array()
                 return 

        #Check for * signs
        if '*' in input_array:
             
             find_all_of_multiplay_signs(input_array)

             #Return the output if are only two numbers for instance 10*5
             if len(input_array) == 1:
                 input_.delete(0, END)
                 input_.insert(0,str(input_array[0]))
                 clear_global_input_array()
                 return 
             
     
             
        #Add operation
        if(input_array[1] == '+'):
            try:
                result = int(input_array[0]) + int(input_array[2])
            except:
                result = float(input_array[0]) + float(input_array[2])            
            input_array = input_array[2:]
            input_array[0] = result
            
            result = 0
        
        #Substract operation
        elif(input_array[1] == '-'):
            try:
                result = int(input_array[0]) - int(input_array[2])
            except:
                result = float(input_array[0]) - float(input_array[2])
            
            input_array = input_array[2:]
            input_array[0] = result
            
            result = 0
        
        if len(input_array) == 1:
            input_.delete(0, END)
            input_.insert(0,str(input_array[0]))
            output = input_.get()
            
            logging.debug(f"Wynik : {output} , Pamięć tablicy : {input_array}")
            
            clear_global_input_array()

def clear_input():
    global input_array
    input_.delete(0, END)
    input_array = []
    return input_array
    
def clear_global_input_array():
    global input_array
    input_array = []

# From 1 to 9
buttons = []

for i in range(1, 10):
    button = Button(root, text=str(i), padx=30, pady=30, fg='black', command=lambda i=i: numbers(i))
    buttons.append(button)

# Placing buttons
for i, button in enumerate(buttons):
    button.grid(row=i // 3 + 1, column=i % 3)

root.mainloop()
