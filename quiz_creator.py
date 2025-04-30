#BEGIN

#Display a window with two options: [Create Quiz] and [Take Quiz]

#IF user clicks "Create Quiz":
    #Repeat the following steps for each question entry:
        #1. Ask the user to type the quiz question
        #2. Ask the user to enter choices for a, b, c, and d
        #3. Ask the user to specify the correct answer (a, b, c, or d)
        #4. Append the question, choices, and correct answer to a text file in a structured format
        #5. Provide an option to go back to the main menu

#IF user clicks "Take Quiz":
    #1. Read all questions, choices, and answers from the text file
    #2. Shuffle the list of questions randomly
    #3. For each question:
        #a. Display the question and choices on the screen
        #b. Wait for the user to click their answer (a, b, c, or d)
        #c. Check if the chosen answer matches the correct one
        #d. Keep track of the number of correct answers
    #4. After all questions are answered, display the final score 

#Provide a "Back to Menu" button in both modes to return to the main screen

#END