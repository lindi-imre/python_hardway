#-*- coding: utf-8 -*-
__author__ = 'Imre'

my_name = 'Lindi Imre'
my_age = 25 # not a lie
my_height = 75 # inches
my_weight = 180 # lbs
my_eyes = 'Brown'
my_teeth = 'Fehér'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (
    30, 40, 50, 120))
