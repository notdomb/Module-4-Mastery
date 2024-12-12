file_path = "C:/Users/Noah/OneDrive/Documents/School/Fall-Semester-24/Programming-Logic-and-Design/M4-Mastery/learning_python.txt"

print("\nReading the entire file at once:")
with open(file_path, "r") as file:
    content = file.read()
    print(content)

print("\nReading the file line by line using a loop:")
with open(file_path, "r") as file:
    for line in file:
        print(line.strip())

print("\nReading the file into a list and processing outside the 'with' block:")
with open(file_path, "r") as file:
    lines = file.readlines()
for line in lines:
    print(line.strip())

replacement_language = "PHP"
print("\nReplacing 'Python' with '{}' and printing each line:".format(replacement_language))
with open(file_path, "r") as file:
    for line in file:
        modified_line = line.replace("Python", replacement_language)
        print(modified_line.strip())
