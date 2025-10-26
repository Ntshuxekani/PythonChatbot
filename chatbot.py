# Simple Chatbot Quiz using Conditional Statements, Data Types, and Data Structures

print("🤖 Hello! Welcome to the Tech Quiz Chatbot.")
name = input("🤖 What is your name? ").strip().title()
print(f"🤖 Welcome, {name}! Let's test your tech knowledge.")

print("\n🤖 Please choose a topic:")
print("1. Python")
print("2. HTML")
print("3. CSS")
print("4. JavaScript")
print("5. Artificial Intelligence")

topic = input("🤖 Which topic are you interested in? ").lower().strip()

# Quiz data: each topic has questions, options, and correct answers
quizzes = {
    "python": {
        "questions": [
            "1. What keyword is used to define a function in Python?",
            "2. What symbol is used for comments in Python?",
            "3. Which data type is this: [1, 2, 3]?",
            "4. What keyword is used to create a loop that repeats a set number of times?",
            "5. What function is used to display output?"
        ],
        "options": [
            ["A) func", "B) define", "C) def", "D) function"],
            ["A) //", "B) #", "C) /*", "D) <!--"],
            ["A) tuple", "B) list", "C) dictionary", "D) set"],
            ["A) for", "B) while", "C) repeat", "D) loop"],
            ["A) echo", "B) log", "C) print", "D) output"]
        ],
        "answers": ["c", "b", "b", "a", "c"]
    },
    "html": {
        "questions": [
            "1. What does HTML stand for?",
            "2. Which tag is used for the largest heading?",
            "3. What tag is used to create a hyperlink?",
            "4. What tag is used to insert an image?",
            "5. Which tag is used for paragraph text?"
        ],
        "options": [
            ["A) HyperText Markup Language", "B) Hyperlinks and Text Markup Language", "C) Home Tool Markup Language", "D) Hyper Tool Markdown Language"],
            ["A) <h6>", "B) <h1>", "C) <head>", "D) <header>"],
            ["A) <a>", "B) <p>", "C) <link>", "D) <href>"],
            ["A) <picture>", "B) <src>", "C) <img>", "D) <image>"],
            ["A) <text>", "B) <para>", "C) <section>", "D) <p>"]
        ],
        "answers": ["a", "b", "a", "c", "d"]
    },
    "css": {
        "questions": [
            "1. What does CSS stand for?",
            "2. Which property changes the background color?",
            "3. Which property changes the text color?",
            "4. How do you select an element with the id 'main'?",
            "5. Which property changes the font size?"
        ],
        "options": [
            ["A) Cascading Style Sheets", "B) Creative Style System", "C) Computer Styled Sections", "D) Colorful Style Sheets"],
            ["A) color", "B) background-color", "C) bg-color", "D) back-color"],
            ["A) text-color", "B) font-color", "C) color", "D) word-color"],
            ["A) .main", "B) #main", "C) main", "D) *main"],
            ["A) font-size", "B) text-size", "C) size", "D) letter-size"]
        ],
        "answers": ["a", "b", "c", "b", "a"]
    },
    "javascript": {
        "questions": [
            "1. What keyword is used to declare a variable?",
            "2. What symbol is used for comments in JavaScript?",
            "3. What function displays a message box?",
            "4. Which operator is used for equality comparison?",
            "5. What keyword is used for a conditional statement?"
        ],
        "options": [
            ["A) let", "B) var", "C) const", "D) All of the above"],
            ["A) //", "B) #", "C) <!--", "D) %%"],
            ["A) show()", "B) display()", "C) alert()", "D) prompt()"],
            ["A) =", "B) ===", "C) ==", "D) <>"],
            ["A) else", "B) if", "C) switch", "D) case"]
        ],
        "answers": ["d", "a", "c", "c", "b"]
    },
    "artificial intelligence": {
        "questions": [
            "1. What does AI stand for?",
            "2. Which field focuses on understanding and processing human language?",
            "3. What is the term for a computer system that can learn from data?",
            "4. What branch deals with training models using labeled data?",
            "5. Name one AI-powered virtual assistant."
        ],
        "options": [
            ["A) Automated Input", "B) Artificial Intelligence", "C) Auto Interaction", "D) Advanced Information"],
            ["A) Machine Learning", "B) Deep Learning", "C) Natural Language Processing", "D) Robotics"],
            ["A) Data Mining", "B) Machine Learning", "C) Data Science", "D) Programming"],
            ["A) Supervised Learning", "B) Unsupervised Learning", "C) Reinforcement Learning", "D) Deep Learning"],
            ["A) Alexa", "B) Siri", "C) Google Assistant", "D) All of the above"]
        ],
        "answers": ["b", "c", "b", "a", "d"]
    }
}

score = 0

if topic in quizzes:
    quiz = quizzes[topic]
    print(f"\n🤖 Great choice, {name}! Let's start your {topic.title()} quiz.\n")

    # Ask 5 questions manually (no loops — only conditionals)
    print(quiz["questions"][0])
    print("\n".join(quiz["options"][0]))
    if input("Your answer: ").lower().strip() == quiz["answers"][0]:
        score += 1

    print("\n" + quiz["questions"][1])
    print("\n".join(quiz["options"][1]))
    if input("Your answer: ").lower().strip() == quiz["answers"][1]:
        score += 1

    print("\n" + quiz["questions"][2])
    print("\n".join(quiz["options"][2]))
    if input("Your answer: ").lower().strip() == quiz["answers"][2]:
        score += 1

    print("\n" + quiz["questions"][3])
    print("\n".join(quiz["options"][3]))
    if input("Your answer: ").lower().strip() == quiz["answers"][3]:
        score += 1

    print("\n" + quiz["questions"][4])
    print("\n".join(quiz["options"][4]))
    if input("Your answer: ").lower().strip() == quiz["answers"][4]:
        score += 1

    print(f"\n🤖 {name}, your total score is {score}/5.")

    if score == 5:
        print("🌟 Excellent work! You really know your stuff!")
    elif score >= 3:
        print("👍 Good job! You have a solid understanding.")
    else:
        print("💪 Keep learning! You’ll do better next time.")

    again = input("\n🤖 Would you like to try another topic? (yes/no): ").lower().strip()
    if again == "yes":
        print("\n🤖 Restart the program to pick another topic! 🚀")
    else:
        print(f"\n🤖 Thank you for playing, {name}! 👋 Have a great day!")

else:
    print("🤖 Sorry, that topic is not available.")
