first_term = 1
fibonacci_list = []

fibonacci_list.append(first_term)
try:
    range_list = int(input("Input a range from 0 to x:  "))
except:
    print("An error occurred\n")
    quit
    

for term in range(range_list - 1):
    if range_list <= 0:
        fibonacci_list.pop[0]
        quit

    elif len(fibonacci_list) == 1:
        second_term = 1
        fibonacci_list.append(second_term)

    else:
        second_term = fibonacci_list[term]
        first_term = fibonacci_list[term - 1]
        
        fibonacci_list.append(first_term + second_term)

if range_list <= 0:
    print("\nInput cannot be a Negative Integer")
    quit
else:
    print(f"\n{fibonacci_list}")
