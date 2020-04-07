questions = [
    {
        "S.No": 1,
        "Question": "What's your country name: ",
        "Option": ["Pakistan", 'U.K', 'Germany', 'Turkey'],
        "Answer": "Pakistan"
    },
    {,
        "Question": "What's your cuty name: ",
        "S.No": 2
        "Option": ["Lahor", 'Karachi', 'Islamabad', 'Talagang'],
        "Answer": "Talagang"
    },
    {
        "S.No": 3,
        "Question": "What's the Capital of Pakistan: ",
        "Option": ["Lahor", 'Karachi', 'Islamabad', 'Talagang'],
        "Answer": "Islamabad"
    }
]

score = 0
for que in questions:
    data = str(que["S.No"]) + ': ' + que["Question"] + "\n " + "Please Enter the Correct answer in the given field" + "\n" + que["Option"][0] + "\n" + que["Option"][1] + "\n" + que["Option"][2] + "\n" + que["Option"][3] + "\n"
    Answer = input(data)
    if Answer == que["Answer"]:
        score += 1

print("You're Score is: " + str(score))