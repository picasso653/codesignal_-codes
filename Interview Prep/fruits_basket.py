# This code will create a simplified fruit salad with the provided fruits
fruits = ['apple', 'banana', 'cherry', 'date']
fruits_in_salad = ""

index = 0
while index < len(fruits):
# Hint: Consider using a conditional to determine when to add a space
    if index == len(fruits) - 1:
        fruits_in_salad += fruits[index]
    else:
        fruits_in_salad += fruits[index] + " "
    index +=1

print(fruits_in_salad)  # Output the fruits in the salad