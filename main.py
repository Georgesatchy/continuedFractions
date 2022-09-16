def gcd(num1, num2):
    maximum = 0
    for n in range(0, num1):
        if num2//n == num2/n:
            maximum = n
    return maximum


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.gcd = 0

    def simplify(self):
        self.gcd = gcd(self.num, self.dem)
        if gcd(self.num, self.dem) > 1:
            return Fraction(self.num/gcd, self.den/gcd)

    def __add__(self, add):
        if isinstance(add, Fraction):
            num = self.num*add.den + self.den*add.num
            den = self.den*add.den
            return self.simplify(Fraction(num, den))
        else:
            return Fraction(self.num + add*self.den, self.den)

    def reciprocal(self):
        return Fraction(self.den, self.num)

    def __str__(self):
        return f"{self.num}/{self.den}"


class ContinuedFraction:
    def __init__(self, values):
        if not isinstance(values, list) or len(values) < 2:
            raise ValueError
        self.values = values
        self.frac = self.fraction()

    def fraction(self):
        total = Fraction(self.values[-1], 1)
        for digit in (self.values[::-1])[1:]:
            total = total.reciprocal() + digit
        return total

    def __str__(self):
        output = f"[{self.values[0]}; {self.values[1]}"
        for n in range(2, len(self.values)):
            output += f", {self.values[n]}"
        output += "]"
        return output


frac = ContinuedFraction([1, 5, 6, 4, 5])
frac = frac.fraction()
print(frac)
