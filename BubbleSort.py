

def Bubble(array=[0, 1]):
    """Function to implement a bubble sort on a list"""
    shifted = True
    while shifted is True:
        for i in range(len(array)):
            for i in range(0, len(array)-i-1):
                i = int(i)
                if int(array[i]) > int(array[i + 1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    shifted = True
                else:
                    shifted = False

    return " ".join(array)


if __name__ == "__main__":
     with open("arrays.txt") as arrays:
         iter = 1
         for array in arrays:
             originalArray = array.rstrip("\n")
             array = array.rstrip("\n").split(" ")
             print(f"Array {iter}")
             print(f"Input: {originalArray}")
             print(f"Output: {Bubble(array)}\n\n")
             iter += 1
         input("Press Enter to quit...")
