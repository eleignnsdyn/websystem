accounts = [
    ("mel","galat"),
    ("nelgie","sdyn"),
    ("glaipam","1026"),
    ("keikei","0220"),
    ("samrograno","5221")
    ]

def menu():
    print("cheezies")
    print("1. Left or Right?")
    print("2. Axis Quiz Game")
    print("3. Lists")
    print("4. Tuples")
    print("5. Functions")
    choice=int(input("Select a program 1-5, 0 to Exit: "))


    if choice == 1:
        print("You Select Conditional Statements")
        cond_statements()

    elif choice == 2:
        print("You Select Loops")
        axis_quiz_game()

def cond_statements():
    print("You are in a dark forest 🌲")
    choice = input("Do you go LEFT or RIGHT? ").lower()

    if choice == "left":
        print("You found a treasure chest! 💰")
        action = input("Do you OPEN it or LEAVE it? ").lower()
        
        if action == "open":
            print("Congrats! You found gold coins! 🪙")
        else:
            print("You walked away safely, but missed the treasure.")
            
    elif choice == "right":
        print("Oh no! You encountered a wild animal 🐺")
        action = input("Do you RUN or FIGHT? ").lower()
        
        if action == "run":
            print("You escaped safely! 🏃")
        else:
            print("The animal was too strong. Game Over 💀")
            
    else:
        print("Invalid choice. You got lost in the forest.")


def axis_quiz_game():
    score = 0

    for question, correct_answer, choices in quiz:
        print("\n" + question)

        for choice in choices:
            print(choice)

        answer = input("Your answer (a/b/c): ").upper()

        if answer == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    return score


# -------------------------------
def show_result(score, total):
    print("\n🎯 Quiz Finished!")
    print(f"Your score: {score}/{total}")
    main_menu()

    if score == total:
        print("🏆 Perfect score, You Did A Insanely Good Job!")
    elif score >= total // 2:
        print("👍 Good job, Atleast You Still Passed!")
    else:
        print("📚 Your Score Is Not Good, Keep Practicing!")


# -------------------------------
quiz = [
    ("1. What is Conditional Statement?", "A",
     ["A) Programs often need to make decisions",
      "B) Computes the result of an expression",
      "C) Symbolic name for a value stored in memory."]),

    ("2. Which is NOT a Python data type?", "C",
     ["A) int", "B) bool", "C) LinkedList"]),

    ("3. Which symbol is used to add numbers?", "B",
     ["A) -", "B) +", "C) *"]),

    ("4. Who created Python?", "A",
     ["A) Guido van Rossum", "B) James Gosling", "C)  Ramus Lerdorf"]),

    ("5. What computes expressions based on precedence?", "A",
     ["A) Expression", "B) Logical", "C) Comparison"]),
]


username = input("Enter your username: ")
password = input("Enter your password: ")

for acc in accounts:
    if username == acc[0] and password == acc[1]:
        print(f"Welcome, {username}")
        menu()
        found = True
        break

if not found:
    print("Invalid username and password!")
