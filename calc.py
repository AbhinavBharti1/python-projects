def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

def divide(x,y):
    return(x/y)

no1 = eval(input("enter the first number = "))
no2 = eval(input("enter the second number = "))

print("select the option")
print("1. addition")
print("2. substraction")
print("3. multiplication")
print("4. division")
print("1. exit")

while(True):
    choice = int(input("enter the choice from 1,2,3,4,5 --> "))
    if choice in (1,2,3,4,5):
      if choice ==1 :
        print("answer", add(no1,no2))
      elif choice ==2 :
        print("answer", subtract(no1,no2))
      elif choice ==3 :
        print("answer", multiply(no1,no2))
      elif choice ==4 :
        print("answer", divide(no1,no2))
      elif choice ==5 :
        exit()
    else:
       print("invalidchoice")