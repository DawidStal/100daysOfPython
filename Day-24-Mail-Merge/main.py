# For each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Day-24-Mail-Merge\\Input\\Letters\\starting_letter.txt", "r") as file:
    content = file.read()

names = open("Day-24-Mail-Merge\\Input\\Names\\invited_names.txt", "r")

for name in names.readlines():
    with open(f"Day-24-Mail-Merge\\Output\\ReadyToSend\\letter_{name.strip()}.txt", mode="w") as letter:
        letter.write(content.replace("[name]", name.strip()))
