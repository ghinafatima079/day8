# Write a function called sum_numbers that takes two numbers as arguments and returns their sum.
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
def sum_numbers(num1,num2):
    return num1+num2
sum=sum_numbers(num1,num2)
print(f"The sum of {num1} and {num2} is {sum}.")

# Create a function called grade_converter that takes a numerical grade as an argument 
# and returns the corresponding letter grade (A, B, C, D, F) based on the standard grading scale.
def grade_converter(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=60:
        return 'D'
    elif score>=50:
        return 'E'
    else:
        return 'F'
score=float(input("Enter your score:"))
grade=grade_converter(score)
print(f"Your grade is {grade}.")

# Write a Python program that defines a function called outer_function.
# Inside outer_function, declare a variable x with a value of 10. 
# Then, define another function called inner_function inside outer_function. 
# Inside inner_function, declare a variable y with a value of 5. 
# Return the sum of x and y from inner_function. Finally, call outer_function and print the result.
def outer_function():
    x=10
    def inner_function():
        y=5
        return x+y
    sum=inner_function()
    return sum
function_call=outer_function()
print("The sum is",function_call)