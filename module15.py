# Module for Assignment Python Chapter 3.5

def printName(name):
    print(f"Hello {name}!")

def printArea(length, width):
    print(f"The area of the house is {length*width}")

def printCircumference(diameter): 
    print(f"Circumference is pi times diameter. So your circumference is {3.14*diameter}")




# For safekeeping. Commenting shopping program here

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

# list = []

# def startProgram():
#     answer = input("What do you want to do? Show/Add/Delete/Quit ")
#     if answer.casefold() == "show":
#         print(list)
#         startProgram()
#     if answer.casefold() == "add":
#         add_input = input("What do you want to add? ")
#         list.append(add_input.title())
#         startProgram()
#     if answer.casefold() == "delete":
#         del_input = input("What do you want to delete? ")
#         list.remove(del_input.title())
#         startProgram()
#     if answer.casefold() == "quit":
#         print("Ok here is your final list.")
#         print(list)
        
# startProgram()