# Write a Python program that performs basic numeric operations and string concatenation. 
# Create a program that: - Accepts two numeric inputs from the user. 
# Performs addition, subtraction, multiplication and division operations on the numeric inputs. 
# Concatenates the two inputs as strings and prints the result.

Number_1 = 4
Number_2 = 0
print("\r")
print("Arithametic operations");
print("\r")

#Addition
print("Addition :-" ,Number_1,"+" ,Number_2,"=",Number_1 + Number_2)

# Subtraction
print("Subtraction :-" ,Number_1,"-" ,Number_2,"=",Number_1 - Number_2)

# Multiplication
print("Multiplication :-" ,Number_1,"x" ,Number_2,"=",Number_1 * Number_2)

# Division
if Number_2 != 0:
    print("Division :-" ,Number_1,"÷" ,Number_2,"=", Number_1 / Number_2 )

else :
    print("Division :- Undefined (Division by zero)")
    print("\r")

# Concatenates the two inputs as strings
Concatenates = str(Number_1) + str(Number_2);
print("Concatenate")
print("\r")

print(Number_1 ,"+", Number_2,"=",Concatenates);
print("\r")

