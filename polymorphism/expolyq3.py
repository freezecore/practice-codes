'''class Calculator:
    def add(self, a, b):
        return a + b

class AdvancedCalculator(Calculator):
    def add(self, a, b, c):
        return a + b + c

def perform_addition(calc, *args):
    return calc.add(*args)

basic = Calculator()
advanced = AdvancedCalculator()

print(perform_addition(basic, 2, 3))        
print(perform_addition(advanced, 2, 3, 4))
'''

