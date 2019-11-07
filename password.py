# Problem set 9 problem 1 

## don't need to return lists 
import string 
# string libary on Python website
import random
# has the random function

def random1(passlength):
    ## return a character form a defined string
    ## could hard code string
    ## string.ascii_letters -> list of capital and lower case letters
    ## string.digits -> all numbers 0-9
    ## string.punctuation -> special characters
    ## string.whitspace -> adds spaces and line feed
    characters = string.ascii_letters + string.digits + string.punctuation
    ## randint inclusive like 0-55
    ## randrange excludes last number
    # for i in range(50):
        # randomNumber = random.randint(0,len(characters) - 1)
        # print(randomNumber)

    password = ''
    for i in range(passlength):
        randomNumber = random.randint(0,len(characters) - 1)
        # print(random1())
        ## adds each random character to the string
        password += characters[randomNumber]
    

    return password

def main():
    passlength = int(input('Enter length of password: '))
    numberOfPasswords= int(input('Enter how many of password: '))

    pwFile = open('Passwords.tx', 'w')

    for i in range(numberOfPasswords):
        password = random1(passlength)
        print(password)
        pwFile.write(password + '\n')

    pwFile.close()

main()

