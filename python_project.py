# I'm attempting to ask the user a question to begin their process with this self-reflection journal
def question_one():
    print "How well do you know yourself?"
# Naturally, I want the user to provide their response in a fill-in box
    fill_in = raw_input("Enter your answer: ")
    print "Response archived!"
question_one()

# I originally wrote the next two questions under the first function but it didn't seem to work so I separated them
def question_two():
    print "What are at least four or five things you are definitely certain about yourself?"
    second_fill_in = raw_input("Enter your answer: ")
# I want to encourage the user's introspection further so I made this reactive response after they fill in their prompt.
    print "Response archived! Think about the things you're uncertain about yourself and explore those parts more."
question_two()

# The third question is supposed to somewhat relate to the second and first question and wraps up the prompts for the day
def question_three():
    print "What are at least two or three traits you used to exhibit that you no longer do?"
    third_fill_in = raw_input("Enter your answer: ")
# I also added another reactive response for their fill-in to boost the user's self-confidence!
    print "Response archived! Be proud of how far you've come and how much growth is ahead of you."
question_three()

journal_archive = open("Your Journal.txt", "r")
journal_archive = close()
