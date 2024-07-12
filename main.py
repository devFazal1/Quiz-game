print("Welcome to Computer Quiz game!")

user_choice = input("Do you want to play? type(yes/no) :  ")
score = 0

if user_choice.lower() != "yes" :
    quit()

print("Let's continue: ")

question1 = input("When Pakistan become a country? ") 
if question1 == '1947': 
    print("correct Answer!")
    score += 1
else:
    print("Wrong Answer!")

question2 = input("What is the main color of Pakistan's Flag?  ") 
if question2.lower() == 'green': 
    print("correct Answer!")
    score += 1
else:
    print("Wrong Answer!")


question3 = input("How many provinces are there in Pakistan?  ") 
if question3 == '4': 
    print("correct Answer!")
    score += 1
else:
    print("Wrong Answer!")

question4 = input("When was first World War fought? ") 
if question4 == '1918': 
    print("correct Answer!")
    score += 1
else:
    print("Wrong Answer!")

question5 = input("When was founder of Pakistan was born? ") 
if question5 == '1876': 
    print("correct Answer!")
    score += 1
else:
    print("Wrong Answer!")


print("You got " + str(score) + " question right.")
