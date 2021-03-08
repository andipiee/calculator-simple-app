import re

print("My Calculator")
print("Type 'quit' to exit")

previous = 0
run = True

def perform_math():
    global run
    global previous

    if previous == 0:
        equation = input("Enter equatation: ")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Goodbye, Human!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()
