#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("./Input/Names/invited_names.txt", "r") as name:
    name_list = name.readlines()
    print(name_list)
    with open("./Input/Letters/starting_letter.txt", "r") as letter:
        content = letter.read()
        for one_name in name_list:
            new_content = content.replace("[name]", f"{one_name.strip()}")
            with open(f"./Output/ReadyToSend/{one_name.strip()}.txt", "w") as fp:
                fp.write(new_content)

