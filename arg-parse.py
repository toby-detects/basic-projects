import argparse

def multiply(num1, num2):
    print(f"{num1} x {num2} =", end=" ")
    print(num1*num2)

def addition(num1, num2):
    print(f"{num1} + {num2} =", end=" ")
    print(num1+num2)

def division(num1, num2):
    print(f"{num1} / {num2} =", end=" ")
    print(num1/num2)

def subtraction(num1,num2):
    print(f"{num1} - {num2} =", end=" ")
    print(num1+num2)

parser = argparse.ArgumentParser(
                    description='BASIC MATH'
                    )
parser.add_argument(
                    'num1',
                    type=int,
                    help='Enter your integer'
                    )
parser.add_argument(
                    'operation',
                    choices=["+","/","-","x"],
                    help='Select your operation'
                    )
parser.add_argument(
                    'num2',
                    type=int,
                    help='Enter your integer'
                    )


args = parser.parse_args()


if args.operation == "+":
    addition(args.num1, args.num2)
elif args.operation == "/":
    division(args.num1, args.num2)
elif args.operation ==  "-":
    subtraction(args.num1, args.num2)
elif args.operation == "x":
    multiply(args.num1, args.num2)