try:
    10 / 0
    c = "I will never get defined"

except ZeroDivisionError:
    try:
        print(c)

    except ValueError:
        print("Error")
