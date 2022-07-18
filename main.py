
with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    
with open("./Input/Letters/starting_letter.txt") as letter:
    text = letter.read()
    for strip_name in names_list:
        name = strip_name.strip('\n')
        replace_text = text.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as all_letters:
            all_letters.write(replace_text)

