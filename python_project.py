# I'm attempting to ask the user a question to begin their process with this self-reflection journal
def questions():
    print "How well do you know yourself?"
# Naturally, I want the user to provide their response in a fill-in box
    fill_in = raw_input("Enter your answer: ")
    print "Response archived!"

    print "What are at least four or five things you are definitely certain about yourself?"
    second_fill_in = raw_input("Enter your answer: ")
# I want to encourage the user's introspection further so I made this reactive response after they fill in their prompt.
    print "Response archived! Think about the things you're uncertain about yourself and explore those parts more."

# The third question is supposed to somewhat relate to the second and first question and wraps up the prompts for the day
    print "What are at least two or three traits you used to exhibit that you no longer do?"
    third_fill_in = raw_input("Enter your answer: ")
# I also added another reactive response for their fill-in to boost the user's self-confidence!
    print "Response archived! Be proud of how far you've come and how much growth is ahead of you."
questions()
# From the link you gave me I know I needed to take their input and save it to a file
import sys
# I definied the file name to indicate their archive
journal_archive = "YourJournal.txt"

original = sys.stdout
# I listed their fill-ins as the content of the file so that the user can access it
filecontent = [str(fill_in), str(second_fill_in), str(third_fill_in)]
# I think this opens the file for the user's convenience. This will help with viewing past responses and seeing how far they've come.
with open(journal_archive, "w") as filehandle:
    sys.stdout = filehandle

    for line in filecontent:
        print(line)

    sys.stdout = original
