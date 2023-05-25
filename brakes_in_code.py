def check_brackets(string: str)-> None:

    stack = []
    flag = 0
    position = 0
    collect = {')': '(',
               ']': '[',
               '}': '{'}

    for indx, char in enumerate(string, 1):

        # if OPENING bracket:
        if char in list(collect.values()):
            stack.append((char, indx))
            continue

        # if CLOSING bracket:
        elif char in list(collect.keys()):

            # if stack is EMPTY:
            if len(stack) == 0:
                print(indx)
                flag = 1
                break

            # if stack NOT EMPTY:
            else:
                # if last bracket not opening:
                if stack[-1][0] != collect[char]:
                    print(indx)
                    flag = 1
                    break
                # if last bracket in stack is openning -> delet bracket from stack:
                else:
                    stack.pop()
                    continue

    if len(stack) > 0 and flag == 0:
        print(stack[-1][1])
    elif len(stack) == 0 and flag == 0:
        print('Success')

check_brackets(input())