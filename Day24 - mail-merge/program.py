with open(file="./Input/Letter/starting_letter.txt", mode="r") as letter_model_file:
    letter_model = letter_model_file.read()

with open(file="./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

for name in names:
    normalized_name = name.replace("\n", "")
    with open(file=f"./Output/letter_to_{normalized_name}.txt", mode="w") as output_letter:
        output_letter.write(letter_model.replace("[name]", normalized_name))
