"""
Tip calculator app
"""

meal = 30.0
tax = 0.0925
tip = 0.15
tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "The base cost of your meal was $%.2f" % meal
print "You need to pay $%.2f for tax" % tax_value
print "Tipping at a rate of %s%%, you should leave $%.2f for a tip." \
    % (tax * 100, tip_value)
print "The grand total of your meal is $%.2f" % total