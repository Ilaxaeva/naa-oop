print ('salam')
num1= float (input("Enter first number"))
num2= float (input("Enter second number"))
print ("Operation: +, -, *, /")
select= input("Select operations")
if select == "+":
  print (num1, "+", num2, "=", add (num1 + num2))
     elif select == "-":
  print (num1, "-", num2, "=", subtract(num1 - num2))
     elif select == "*":
     print (num1, "*", num2, "=", multiply(num1 * num2))
     elif select == "/":
      print (num1, "/", num2, "=", multiply(num1 / num2))
      else:
      print ("input")