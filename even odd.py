a = input("PLease Enter a Number: ") as type(int)
a = int(a)

while type(a) == int:
        if(a % 2 == 0):
                print("{} is Even".format(a))
                a = input("Enter another number: ")
                a = int(a)

        elif(a % 2 != 0):
                print("{} is Odd".format(a))
                a = input("Enter another number: ")
                a = int(a)

print("That isn`t a number silly...")
input("Enter a real number this time: ")

                
        






