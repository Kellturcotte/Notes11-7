# This is how you can get a user input to call a function 


def rock():
    print('Rock')

def paper():
    print('Paper')

def scissors():
    print('Scissors')

def main():
    which = input('Enter 1 for rock, 2 for paper, 3 for scissors')
    if which == 1:
        rock()
    elif which == 2:
        paper()
    elif which == 3:
        scissors()
    else:
        print('Error')
