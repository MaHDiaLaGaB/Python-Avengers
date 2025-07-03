"""
read the file line by line fix the 
file content to be in good structure 
"""


notes = "4- we will work. \n5- eat launch. \n6- go to home."

with open("data/note.txt", "a", encoding="utf-8") as note_file:
    note_file.write(notes)


with open("data/note.txt", "r", encoding="utf-8") as f:
    """finish the code here """
    print(f.readlines())