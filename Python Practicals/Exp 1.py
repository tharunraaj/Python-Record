name=input('Enter Student name:')
subj=int(input('Enter number of subjects:'))
total=0

for i in range(1,subj+1):
    mark=float(input('Enter mark:'))
    total+=mark
percentage=total/subj
print(percentage)
if percentage >= 90:
    grade = "A+"
    performance = "Outstanding"
elif percentage >= 80:
    grade = "A"
    performance = "Excellent"
elif percentage >= 70:
    grade = "B"
    performance = "Very Good"
elif percentage>=60:
    grade="C"
    performance="Good"
elif percentage>=50:
    grade="D"
    perforance='Average'
else:
    grade='F'
    performance="Need to do better"

print("\n--- Academic Performance ---")
print("Student Name :", name)
print("Total Marks :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade :", grade)
print("Performance :", performance)