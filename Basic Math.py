#BASIC CALCULATOR
X=input("Num1:")
Y=input("Num2:")
print("This program can perform 4 operations:\n1. Addition(+)\n2. Subtraction(-)\n3. Muliplication(*)\n4. Division(/)\n")
Answer=input("Which one do you wish to perform?\n")
if Answer=="1":
        print(int(X) + int(Y))
elif Answer=="2":
        print(int(X) - int(Y))
elif Answer=="3":
        print(int(X) * int(Y))
elif Answer=="4":
        print(int(X) / int(Y))
else:
        print("INVALID OPERATION")

#MODULO GIVES THE REMAINDER OF THE DIVISION
print(int(X) % int(Y)) #MODULO GIVES A REMAINDER FOR THE DIVISION
print(pow(int (X),int (Y))) #POWER FUNCTIONALITY RAISES ONE NUNBER BY ANOTHER