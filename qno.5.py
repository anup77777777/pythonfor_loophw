marks = int(input("Enter the student's marks: "))
if marks > 90:
    result = "Excellent"
elif marks > 50:
    result = "Good"
else:
    result = "Fail"
print(f"The student's performance is: {result}")
