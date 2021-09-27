import datetime
file = open("scores.txt", "a")
print("Enter your latest score:")
score = int(input())
currenttime = datetime.datetime.now()
timestamp = currenttime.strftime("%d-%m-%Y %H:%M:%S")
newscore = (f"\nScore of {score} recorded at {currenttime}")
file.write(newscore)
file.close()