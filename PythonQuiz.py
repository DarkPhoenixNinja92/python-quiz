print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play. :)")
score = 0

answer = input("What was the windows operating system released in 1998? ")

if answer.lower() == "windows 98":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does PSU stand for? ")

if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What company makes the windows operating system? ")

if answer.lower() == "microsoft":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    score += 1
    print('Correct!')
else:
    print('Incorrect!')

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(f'You got {score} questions right!')