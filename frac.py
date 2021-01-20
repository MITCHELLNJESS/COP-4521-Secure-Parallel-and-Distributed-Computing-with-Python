class Fraction(object):
    def __init__(self, n = 0 , d = 1):
        self.numerator = n
        self.denominator = d

    def input(self):
        frac_input = input().split('/')
        self.numerator = int(frac_input[0])
        self.denominator = int(frac_input[1])

    def show(self):
        print (str(self.numerator) + "/" + str(self.denominator))

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def setValue(self, n, d):
        self.numerator = n
        self.denominator = d

    def evaluate(self):
        return float(self.numerator)/float(self.denominator)
    
