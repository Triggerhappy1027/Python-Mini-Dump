# ask the user to type in a series of integers
# program converts it into a list and reverses them
# it then prints the reversed list

test = input("Enter a series of integers separated by a space: ").split(" ")

test.reverse()
print(test)
print(list(reversed(test)))
