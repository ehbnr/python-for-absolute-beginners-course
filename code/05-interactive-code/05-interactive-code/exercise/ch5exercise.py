#  Chapter 5 exercises

req_num_int = 1

while req_num_int > 0:
    req_num = input("Please choose a number: ")
    req_num_int = int(req_num)

    remainder = req_num_int % 2

    if remainder == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

print("Goodbye!")