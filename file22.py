# Python Exceptions Handling
print("Start")
try:
    x = 10
    y = 0
    if x < 20 :
        z = x / y
        print(z)
    else :
        z = x + y
        print(z)
except ZeroDivisionError as e:
    print("ZeroDivisionError =",e)
except NameError as e:
    print("NameError =",e)
except Exception as e:
    print("Exception =",e)
else:
    print("Else Block")
finally:
    print("In Finally Block")
print("End")
