print("Multiplication Game!\n")
number = int(input("What multiplication table do you wish to answer?\n"))
print("Great! Lets get started...\n")

score = 0

for i in range(1, 11):
    correct_answer = number * i
    user_answer = int(input(f" {i} X {number} =  "))
    if user_answer == correct_answer:
        score += 1
        print("Good Job!")
    else:
        print(
            f"Sorry, that's incorrect. The correct answer is {correct_answer}.")

while True:
    if score == 10:
        print("CONGRATULATIONS!!! YOU GOT A PERFECT SCORE!!!")
    else:
        print(f"you got {score} correct")
    break
