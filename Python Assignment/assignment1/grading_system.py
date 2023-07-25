A=True
while A==True:
    marks=int(input("Marks obtained by student: "))
    if marks<=0:
        print("invalid marks")
        continue
    if marks>=90:
        print("Grade- A+")
    elif 80<=marks<90:
        print("Grade- A")
    elif 70<=marks<80:
        print("Grade- B")
    elif 60<=marks<70:
        print("Grade- C")
    elif 50<=marks<60:
        print("Grade- D")
    elif marks<50:
        print("Fail")
    B=input("Do you want to exit Y/N")
    if B=="Y" or B=="y":
        A=False
