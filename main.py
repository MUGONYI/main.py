def calculate(number1,number2,operation):
    result=0
    if operation=='+':
        result=number1+number2
    if operation=='-':
        result=number1-number2
    if operation=='*':
        result=number1*number2
    if operation=='/':
        result=number1/number2
    print(result)
calculate(3,4,"+")