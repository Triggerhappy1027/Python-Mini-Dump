import math
from math import sqrt

testNum = int(input("Enter any Integer: "))

# Print the square of the number
sqrNum = testNum*testNum
print("{} square is equal to: {}".format(testNum, sqrNum))

if testNum < 0:
	print("{} does not have a Square Root: negative integer".format(testNum))
	quit()

sqrtNum = math.sqrt(testNum)



if sqrtNum % 1 == 0:
	print("{}'s Square Root is equal to: {}".format(testNum, int(sqrtNum)))

else:
	print("{}'s Square Root returns a float".format(testNum))
