# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('Enter the lengths of three side of a triangle:')
side1 = input('side 1:')
side2 = input('side 2:')
side3 = input('side 3:')

if side1 == side2 and side2 == side3:
  print(f'A triangle with sides of {side1}, {side2} & {side3} is an equalateral triangle.')
elif side1 != side2 and side1 != side3 and side2 != side3:
  print(f'A triangle with sides of {side1}, {side2} & {side3} is a scalene triangle.')
else:
  print(f'A triangle with sides of {side1}, {side2} & {side3} is an isosceles triangle.')