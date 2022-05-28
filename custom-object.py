# File 4 - 4.8 - 4.17

# Python Object representing a purchase for a given amount
class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
    
    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0
    
    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100.0
    
    def calculateTotal(self, taxPercent, tipPercent):
            return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)
        
# Create Purchase object given an amount
purchase = Purchase(100.0)

# Set the tax and tip percentages
taxPercent = 7.5
tipPercent = 20.0

# Use the object to calculate tax and tip
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

# Display some useful information
print ('Tax: ', tax)
print ('Tip: ', tip)
print ('Total: ', purchase.calculateTotal(taxPercent, tipPercent))

# Assignment 2
#1
print('Call Function calculateTax():', purchase.calculateTax(7.5))
#2
print('Call Function calculateTip():', purchase.calculateTip(20.0))

print('Erin Swan-Siegel')