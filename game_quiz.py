print("Welcome to the World of Computer Quiz!!!")

wantToPlay = input("Are you intrested in playing? ")

if wantToPlay.lower() != "yes":
    quit() #exits from the python program

print ("Okay! Let's Play :)")
score = 0
#first question
answer = input ("1. What does CPU stands for? ").lower() #converting the input into lower case
if answer == "central processing unit":
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect!")

#second question
answer = input ("2. What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect!")

#third question
answer = input ("3. What does RAM stands for? ").lower()
if answer == "random access memory":
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect!")

#fourth question
answer = input ("4. What does PSU stands for? ").lower()
if answer == "power supply unit":
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect!")

print("You got " + str(score) + " points at the end of the quiz!" )
print("You got "+ str((score/4)*100)+"%.")
print("Congrats!!!")