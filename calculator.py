#since the code is being read from top to bottom you must import at the top
import addition
import subtraction
import multiplication
import division



# i print these so that the user can see what math operation they will go with
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#this is a while loop, different from the for loop in that it will not run 'x' amount of times,
#a while loop runs as a set of code if the condition defined is true 
# here i create the while loop by writing while and then true so that the code statements below
#only execute when true, i add the : to start it up
while True:

#here i define the variable Userchoice, then i put the input function which allows for user input
# i give the user a choice to enter values
    UserChoice = input("Choose (1,2,3,4): ")
#if the users choice is 1 2 3 4 run this code
    if UserChoice in ('1', '2', '3', '4'):
#the code that is run is a input in which the first number is a variable that stores the users input

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
#if the userschoice is equal to one, print the value of num1 concatonate with a string that shows
#that the content was added and concatonate with a = and then run the function that acc does the math
#that is now called back so the value of x, y is now the variables num1 and num2
        if UserChoice == '1':
            print(num1, "+", num2, "=", addition.addNum(num1, num2))

        elif UserChoice == '2':
            print(num1, "-", num2, "=", subtraction.subtractNum(num1, num2))

        elif UserChoice == '3':
            print(num1, "*", num2, "=", multiplication.multiplyNum(num1, num2))

        elif UserChoice == '4':
            print(num1, "/", num2, "=", division.divideNum(num1, num2))
#we use the break to stop the code, otherwise the if the conditions remain true the code
#will run up again, its basically a period i think
        break
    else:
#if they dont chose any print invalid input
        print("pick a num 1 - 4 silly ")