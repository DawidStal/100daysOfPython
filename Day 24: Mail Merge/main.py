# For each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./input/Letters/starting_letter.txt", "r") as file:
    content = file.read()

names = open("./input/Names/invited_names.txt", "r")

for name in names.readlines():
    with open(f"./Output/ReadyToSend/letter_{name.strip()}.txt", mode="a") as letter:
        letter.write(content.replace("[name]", name.strip()))
