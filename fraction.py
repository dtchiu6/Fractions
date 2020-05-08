#function.py
import math


class Fraction:

    def __init__(self, a, b):
        self.num = a
        self.den = b
        self.simplify()

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def approximate(self):
        return "{0:.8f}".format(self.num / self.den)

    def simplify(self):
        x = self.gcd(self.num, self.den)
        self.num = self.num // x
        self.den = self.den // x

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def __add__(self,other):
        num = (self.num * other.den) + (other.num * self.den)
        den = (self.den * other.den)
        return Fraction(num, den)
    
    def __sub__(self,other):
        num = (self.num * other.den) - (other.num * self.den)
        den = (self.den * other.den)
        return Fraction(num, den)
    
    def __mul__(self,other):
        num = (self.num * other.num)
        den = (self.den * other.den)
        return Fraction(num, den)
    
    def __truediv__(self,other):
        num = (self.num * other.den)
        den = (self.den * other.num)
        return Fraction(num, den)
    
    def __pow__(self,exp):
        if exp < 0:
            return Fraction(self.den, self.num) ** exp
        elif exp == 0:
            return Fraction(1, 1)
        else:
            return Fraction(self.num, self.den) * Fraction(self.num, self.den) ** (exp-1)
    
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.num == other.num and self.den == other.den
        
        