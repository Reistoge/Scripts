# ask the user to enter a line of text
input = input()
# check if the input contains a smiley face and assign a boolean value to smiley
smiley = ":)" in input
# check if the input contains a frowny face and assign a boolean value to frowny
frowny = ":(" in input
#accepts only ints not strings
# use if-elif-else statements to output one of the four words based on the values of smiley and frowny
if smiley and not frowny:
  print("alive")
elif not smiley and frowny:
  print("undead")
elif smiley and frowny:
  print("double agent")
else:
  print("machine")