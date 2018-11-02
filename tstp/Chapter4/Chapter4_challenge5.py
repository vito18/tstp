def str_float(a):
    try:
        return float(a)
    except ValueError:
        print("Value Error!")   

_input = input("enter soomething: ")
b = str_float(_input)
print(b)
