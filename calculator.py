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