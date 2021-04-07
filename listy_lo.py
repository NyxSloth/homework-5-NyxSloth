
if __name__ == "__main__":

# Create a list named food with two elements 'rice' and 'beans'.
    food = ['rice','beans']

# Append the string 'broccoli' to food using .append().
    food.append('broccoli')
    print(food)

# Add the strings 'bread' and 'pizza' to food using .extend().
    food1 = ['bread','piza']
    food.extend(food1)
    print(food)

# Print the first two items in the food list using print() and slicing notation.
    print(food[0:2])

# Print the last item in food using print() and index notation.
    print(food[-1])

# Create a list called breakfast from the string "eggs,fruit,orange juice" using the split() method.
    bfast = "eggs,fruit,orange juice"
    breakfast = bfast.split(',')
    print(breakfast)
    
# Verify that breakfast has 3 elements using the len built-in.
    print(len(breakfast))
    
# prompts the user for a floating-point value until they enter stop. Store their entries in a list, and then find the average, min, and max of their entries and print them those values.
    user_list = []
    user_input = 'start'
    while True:
        user_input = input('Enter a floating-point value. When done, enter stop. ') 
        if user_input == 'stop':
            break
        value = float(user_input)
        user_list.append(user_input)
        print(user_list)
