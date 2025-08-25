from argflow import argflow as argf
argflow = argf()

class Values:
    AppendValue = False
    Result = 0


def add(num1, num2=0):
    value = int(num1) + int(num2)
        
    if Values.AppendValue:
        Values.Result += value
        print(Values.Result)
    else:
        print(value)
        
def sub(num1, num2=0):
    value = int(num1) - int(num2)
        
    if Values.AppendValue:
        Values.Result -= value
        print(Values.Result)
    else:
        print(value)

argflow.new_argument("--append", lambda: setattr(Values, "AppendValue", True))
argflow.new_argument("--add", add, allow_multiple=True)
argflow.new_argument("--sub", sub, allow_multiple=True)
argflow.parse()