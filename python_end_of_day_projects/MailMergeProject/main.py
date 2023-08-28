# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as names:
    inv_names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letters:
    letter = letters.read()
    for n in inv_names:
        stripped_name = n.strip("\n")
        new_letter = letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete:
            complete.write(new_letter)

