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

# --------------------------------------
# Solution for part 2

# print("Let's talk about numbers!")
# print()
#
# num_text = input("What's your favorite whole number? ")
# num = int(num_text)
#
# if num % 2 == 0:
#     print(f"What a sweet number, {num:,} is even!")
# else:
#     print(f"That's odd. Yeah, I mean {num:,} is an odd number mathematically.")
#
# # Note:
# # {num:,} does digit grouping: 10101010 -> 10,101,010
# # {num} would just repeat it as 10101010.

# ----------------------------------------
# Solution for part 3
#
#     print("Let's talk about numbers!")
#     print()
#
#     question_text = "Give me a whole number [0 to cancel]? "
#
#     num_text = input(question_text)
#     num = int(num_text)
#
#     while num != 0:
#
#         if num % 2 == 0:
#             print(f"What a sweet number, {num:,} is even!")
#         else:
#             print(f"That's odd. Yeah, I mean {num:,} is an odd number mathematically.")
#
#         # Note:
#         # {num:,} does digit grouping: 10101010 -> 10,101,010
#         # {num} would just repeat it as 10101010.
#
#         num_text = input(question_text)
#         num = int(num_text)
#
#     print("kthxbye!")