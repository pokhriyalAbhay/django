mul = lambda x,y:x+y
def sum(number):
    print("table number is ")
    for x in range(1,11):
        result = mul(number,x)
        print(f"{number}*{x}={result}")
number = int(input("enter the  number"))
sum(number)