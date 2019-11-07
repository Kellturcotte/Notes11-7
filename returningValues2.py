# can send values without parameters

def pbj(jelly):
    print('I am making a sandwich')
    
    if jelly == 1:
        return 1
    else:
        return 2

def main():
    if pbj(1) == 1:
        print('Sandwich delivered')
    if pbj(2) == 2:
        print('Late delivery')


main()