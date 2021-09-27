file = open("rnj.txt", "r")
a = 0
for line in file:
  for letter in line:
    if letter == "a":
      a = a + 1
file.close()
file = open("rnj.txt", "a")
file.write(f"\n\nLetter: a\nOccurences: {a}")
file.close()