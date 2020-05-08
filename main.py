#main.py
from fraction import Fraction

def H(n):
    h = Fraction(0, 1)
    for k in range(1, n + 1):
        h += Fraction(1, k)
    return h

def T(n):
    t = Fraction(0, 1)
    k = 0
    while(k <= n):
        t += Fraction(1, 2) ** k
        k += 1
    return t

def Z(n):
    z = Fraction(0, 1)
    for k in range(0, n + 1):
        z += Fraction(1, 2) ** k
    return Fraction(2, 1) - z

def R(n, b):
    r = Fraction(0, 1)
    for k in range(1, n + 1):
        r += Fraction(1, k) ** b
    return r

#Main Code

if __name__ == "__main__" :

    print('Welcome to Fun with Fractions!')
    
    valid = False
    while not valid:
        try:
            userInput = int(input("Enter Number of iterations (integer>0):\n"))
            if userInput > 0:
                valid = True
        except ValueError:
            valid = False

    print( 'H(' +str(userInput) + ')=' + str(H(userInput)))
    print( 'H(' +str(userInput) + ')~=' + str(H(userInput).approximate()))
    print( 'T(' +str(userInput) + ')=' + str(T(userInput)))
    print( 'T(' +str(userInput) + ')~=' + str(T(userInput).approximate()))
    print( 'Z(' +str(userInput) + ')=' + str(Z(userInput)))
    print( 'Z(' +str(userInput) + ')~=' + str(Z(userInput).approximate()))
    for i in range(userInput, userInput + 1):
        print( 'R(' + str(userInput) + ',' + str(i) +')=' + str(R(userInput, i)))
        print( 'R(' + str(userInput) + ',' + str(i) +')~=' + str(R(userInput, i).approximate()))
        
