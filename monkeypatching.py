# Original class
class Calculator:
    def add(self, a, b):
        print ("inside old add")
        return a + b

# Create an instance of the original class
calc = Calculator()
print(f"Original add: {calc.add(2, 3)}")

# Define a new function to replace the 'add' method
def new_add(self, a, b):
    print ("inside new add")
    return f"The sum of {a} and {b} is {a + b}"

# Monkey patch the 'add' method of the Calculator class
Calculator.add = new_add

# Call the patched method
print(f"Patched add: {calc.add(2, 3)}")

# You can also patch methods on a specific instance
calc2 = Calculator()
def instance_specific_add(self, a, b):
    return f"Instance-specific sum: {a + b}"

calc2.add = instance_specific_add.__get__(calc2) # Bind the method to the instance
print(f"Instance-specific add: {calc2.add(5, 5)}")

# Original instance still uses the class-level patch
print(f"Original instance after instance patch: {calc.add(1, 1)}")