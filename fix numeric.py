import re
# Open the file in read mode
with open('main.py', 'r') as file:
  lines = file.readlines()

# Open the file in write mode and delete all spaces and digits from the begining of each line.
with open('main.py', 'w') as file:
  for line in lines:
    if re.match("(^\s*\d*)(.*)", line):
       file.write(re.match("(^\s*\d*)(.*)", line).group(2))
    else:
       file.write(line)
    file.write("\n")

