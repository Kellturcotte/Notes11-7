# adding strings with functions

def fred(a,b):
    # theSum = a + b
    # return theSum
    return a + b

def main():
    a = input('Enter a string: ')
    b = input('Enter a string: ')
    
    print(fred(a,b))
    # total = fred(a,b)
    # print(total)
main()

def fred2(a,b,c):
    if c == 1:
        return a + b
    elif c == 0: 
        print(a + b)
    else:
        print('Error')