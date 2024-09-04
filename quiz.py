print("======================")
print("Welcome to my quiz.!")
print("======================")

playing = input("Do you want to play? (yes/no) \n")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is the capital of INDIA? \n")
if answer.lower() == "delhi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the currency of INDIA? \n")
if answer.lower() == "rupee":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Rainbow consist of how many colours? \n")
if answer.lower() == "7":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Name the National bird of India? \n")
if answer.lower() == "peacock":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
print("==============================")
print("You got " + str(score) + " questions correct!")
print("==============================")
