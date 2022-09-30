PLACEHOLDER= "[name]"

with open("./names.txt") as names_file:
    names= names_file.readlines()
    print(names)

with open("./letter.txt") as letter_file:
    letter_contents= letter_file.read()
    for each_name in names:
     stripped_name= each_name.strip()
     new_letter=letter_contents.replace(PLACEHOLDER, stripped_name)
     with open(f"./letter_for_{stripped_name}.txt",mode="w") as final_invitation:
         #python will automatically create a file if it doesnt exist but for that it should be in write mode
         final_invitation.write(new_letter)
     print(new_letter)
