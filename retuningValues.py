# you can change vaules in functions with other functions

def change(o):
    o = 'Olga the insturctor'
    return o


def main():
    olga = 'Instructor'
    which = input('Enter 1 or 2: ')
    if which == 1:
        olga == change(olga)
    if which == 2:
        print('No')
main()