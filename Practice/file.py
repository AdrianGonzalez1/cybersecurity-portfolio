# def greet(name):
#     nickname = name + " The Great"
#     print("Hi " + nickname + "!")

# greet("Adrian")

# def full_greeting(first_name, last_name):
#     return "Hello " + first_name + " " + last_name

# print(full_greeting("Adrian", "Gonzalez"))

# message = full_greeting("Adrian", "Gonzalez") ##This essentially does the same as line above, just better practice to reuse this function throughout code.
# print (message)

# def grade_feedback(grade):
#    if grade >= 90:
#         return "Great job!"
#     elif grade >= 70:
#         return "You passed!"
#     else:
#         return "Keep trying!"@ 
   
# user_input = input("Enter your grade: ") # Ask for the user input
# grade = int(user_input) # converts user input into an integer

# print(grade_feedback(grade)) # calls function and prints result


# def check_answer(answer):
#     if answer.strip().lower() == "mexico":
#         return "Al Cien!"
#     else:
#         return "No eres raza =("
    
# user_input = input("Where were you born? ") # Ask where they were born
# answer = str(user_input)

# print(check_answer(user_input))

# foods = ["Tacos", "Ceviche", "Burritos", "Flautas"]

# for food in foods:
#     print("I want to eat " + food)


foods = []

while True:
    food = input("Enter a food that you like (or type 'done' to finish): ")
    if food.lower() == "done":
        break
    foods.append(food)
print("\nYou said you like:")
for food in foods:
    print("-" + food)
print("\nTotal number of foods you entered:", len(foods))