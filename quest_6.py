score = int(input("Enter your score (0 - 100)"))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
elif score >= 0:
    print("Fail")
else:
    print("Invalid score. Please enter a score between 0 and 100")

   