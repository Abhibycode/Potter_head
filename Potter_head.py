#Potter head

Easy = [
    {
        "prompt": "What is the name of Harry Potter's owl?",
        "options": ["A. Percy", "B. Snowy", "C. Oliver", "D. Hedwig"],
        "Answer": "D"
    },
    {
        "prompt": "Which Hogwarts house is known for its bravery and chivalry?",
        "options": ["A. Ravenclow", "B. Hufflepuff", "C. Gryffindor", "D. Slytherin"],
        "Answer": "C"
    },
    {
        "prompt": "What is the name of the magical train that takes students to Hogwarts?",
        "options": ["A. Hogwarts Express", "B. Night Express", "C. Wizarding Express", "D. Magic Express"],
        "Answer": "A"
    },
    {
        "prompt": "Who is the headmaster of Hogwarts School of Witchcraft and Wizardry?",
        "options": ["A. Minerva McGonagall", "B. Severus Snape", "C. Albus Dumbledore", "D. Rubeus Hagrid"],
        "Answer": "C"
    },
]

Medium = [
    {
        "prompt": "What is the name of the spell that can repair broken bones?",
        "options": ["A. Wingardium Leviosa", "B. Reparo", "C. Expelliarmus", "D. Lumos"],
        "Answer": "B"
    },
    {
        "prompt": "What is the name of the dark wizard who killed Harry's parents?",
        "options": ["A. Lord Voldemort", "B. Bellatrix Lestrange", "C. Draco Malfoy", "D. Lucius Malfoy"],
        "Answer": "A"
    },
    {
        "prompt": "Who is the Half-Blood Prince?",
        "options": ["A. Tom Riddle", "B. Harry Potter", "C. Draco Malfoy", "D. Severus Snape"],
        "Answer": "D"
    },
]


Difficult = [
    {
        "prompt": "What is the name of the magical creature that guards the Philosopher's Stone?",
        "options": ["A. Grawp", "B. Aragog", "C. Fluffy", "D. Norbert"],
        "Answer": "C"
    },
    {
        "prompt": "What is the name of the spell that can produce a Patronus charm?",
        "options": ["A. Stupefy", "B. Incendio", "C. Protego", "D. Expecto Patronum"],
        "Answer": "D"
    },
    {
        "prompt": "What is the name of the magical object that can grant the power of invisibility?",
        "options": ["A. Invisibility Cloak", "B. Resurrection Stone", "C. Elder Wand", "D. Time-Turner"],
        "Answer": "A"
    },
]



def Quiz(Easy, Medium, Difficult):
    Q1 = str(input("Let's find how much of potter head are you\nAre you ready for challenge?(yes/no): "))
    Q2 = str(input("Which level you want to choose?(Easy/Medium/Difficult): ")).upper()
    score = 0
    if Q2 == "EASY":
        for easy in Easy:
            print(easy["prompt"])
            for option in easy["options"]:
                print(option)
            answer = str(input("Enter you choices (A/B/C/D): "))
            if answer == easy["Answer"]:
                "You are good"
                score += 1
            else:
                "No you don't look that good"
        print(f"Your score is: {score}")
        if score == len(Easy):
            print("Seem you are actually Potter Head\n")
        else:
            print("Nope, you ain't our member\n")

    elif Q2 == "MEDIUM":
        for Mid in Medium:
            print(Mid["prompt"])
            for option in Mid["options"]:
                print(option)

            answer = str(input("Enter you choices (A/B/C/D): "))
            if answer == Mid["Answer"]:
                "You are good"
                score += 1
            else:
                "No you don't look that good"
        print(f"Your score is: {score}")
        if score == len(Medium):
            print("Seem you are actually Potter Head\n")
        else:
            print("Nope, you ain't our member\n")

    elif Q2 == "DIFFICULT":
        for diff in Difficult:
            print(diff["prompt"])
            for option in diff["options"]:
                print(option)
            answer = str(input("Enter you choices (A/B/C/D): "))
            if answer == diff["Answer"]:
                "You are good"
                score += 1
            else:
                "No you don't look that good"
        print(f"Your score is: {score}")
        if score == len(Difficult):
            print("Seem you are actually Potter Head\n")
        else:
            print("Nope, you ain't our member\n")



while True:
    Q3 = str(input("You want to play round?(yes or no): ")).upper()
    if Q3 == "YES":
        Quiz(Easy, Medium, Difficult)
    else:
        break