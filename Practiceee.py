name = "Vineetha"
name1="Manoj"
# print(name)
# print(name.__doc__)

def calc(num1,num2,op):

        if op == "+":
            res = num1+num2
        elif op == "-":
            res = num1 - num2
        elif op == "*":
            res = num1*num2
        elif op == "/":
            res = num1/num2
        return res

num1 = float(input("enter 1st munbers\n"))
num2 = float(input("enter 2nd munbers\n"))
op = input("enter operator\n")
print(calc(num1,num2,op))
