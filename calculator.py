#str = "12 * 34 * 56/78"

def div(x, y):
    return int(x) / int(y)

def mult(x, y):
    return int(x) * int(y)

def calculate_first(str):

    previous_operation = None
    for i, char in enumerate(str):

        print(i, char)

        if char == "*":
            left = ""
            right = ""
            print(f"Found * at position {i}")
            pos = i - 1
            while pos >= 0 and str[pos] == " ":
                pos = pos - 1
            while pos >= 0 and isdigit(str[pos]):
                if left == "":
                    left = str[pos]
                else:
                    left = str[pos] + left
                pos = pos - 1
            print("  " + left)

            pos2 = i + 1
            while pos2 != len(str) and str[pos2] == " ":
                pos2 = pos2 + 1
            while pos2 != len(str) - 1 and isdigit(str[pos2]):
                # make a loop to catch all chars after * until the next *,/,+,-  and join them one by one.
                if right == "":
                    right = str[pos2]
                else:
                    right += str[pos2]
                pos2 = pos2 + 1
            print("  " + right)
            print(mult(left, right))

        elif char == "/":
            print(f"I have found / in possition {i}")

        else:
            continue
#str = "11 + 24 + 22 - 15"
#def add(x, y):
#    return int(x) + int(y)
#def substract(x, y):
#    return int(x) - int(y)
#
#def calculator(str):
#    right = ""
#    left = ""
#    previous_operation = None
#    for char in str:
#        if char == " ":
#            continue  # skip spaces
#
#        elif char == "+":
#            if previous_operation == None:
#                # we only build the first left str_number and nw we are building the right one.
#                previous_operation = add
#            else:
#                left = previous_operation(left, right)
#                right = ""
#                # you could execute the last + sum  or - functions as both left and right are build and have - or + in the middle
#                # previous left and righr numbers are in a form of a string
#                # next char would start to build another right number
#                # we have build 11 + 24 already (and also left 71) and now we execute it (34), or just first left "11".
#                previous_operation = add
#
#        elif char == "-":
#            if previous_operation == None:
#                # we only build the first left str_number and nw we are building the right one.
#                previous_operation = substract
#            else:
#                left = previous_operation(left, right)
#                right = ""
#                # you could execute the last + sum  or - functions as both left and right are build and have - or + in the middle
#                # previous left and righr numbers are in a form of a string
#                # next char would start to build another right number
#                # we have build 11 + 24 already (and also left 71) and now we execute it (34), or just first left "11".
#                previous_operation = substract
#        else:
#
#            if left != "" and previous_operation != None:
#                if right != "":
#                    right += char
#                else:
#                    right = char
#
#            elif left != "" and previous_operation == None:
#                left += char
#            else:
#                left = char
#
#    if previous_operation != None:
#        left = previous_operation(left, right)
#
#    print(left)
#    return left
#
#calculator("11 + 24 + 22 - 15")