# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
global msg_5
global msg_index
global M
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
result = 0
M = 0

def is_one_digit(v):
    try:
        if -10 < v < 10 and v.is_integer() == True:
            return True
        else:
            return False
    except AttributeError:
        return True

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)

while True:
    print(msg_0)
    calc = input()
    calc_list = calc.split(' ')
    x = 0
    y = 0

    try:
      if calc_list[0] != "M":
        x = float(calc_list[0])
      elif calc_list[0] == "M":
        x = M
      if calc_list[2] != "M":
        y = float(calc_list[2])
      elif calc_list[2] == "M":
        y = M
    except ValueError:
        print(msg_1)
        continue

    if calc_list[1] not in ('+', '-', '*', '/'):
        print(msg_2)
        continue

    try:
        check(x,y,calc_list[1])
    except ZeroDivisionError:
        continue

    try:
      if calc_list[1] == '+':
        result = x + y
        print(result)
      elif calc_list[1] == '-':
        result = x - y
        print(result)
      elif calc_list[1] == '*':
        result = x * y
        print(result)
      elif calc_list[1] == '/':
        result = x / y
        print(result)
    except ZeroDivisionError:
      print(msg_3)
      continue

    print(msg_4)
    save = input()

    if save == "y":
        if is_one_digit(result) == True:
            msg_index = 10
        elif is_one_digit(result) == False:
            M = result
            print(msg_5)
            cont = input()
            if cont == "y":
                continue
            elif cont == "n":
                break
        while True:
            print(msg_[msg_index])
            cont = input()
            if cont == "y" and msg_index < 12:
                msg_index = msg_index + 1
            elif cont == "n":
                print(msg_5)
                cont = input()
                if cont == "y":
                    break
                elif cont == "n":
                    break
            else:
                M = result
                print(msg_5)
                cont = input()
                if cont == "y":
                    break
                elif cont == "n":
                    break
    elif save == "n":
        print(msg_5)
        cont = input()
        if cont == "y":
            continue
        elif cont == "n":
            break
