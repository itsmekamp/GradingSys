grdList = []

def avg(list):
    return (sum(list) / len(list))

def ord(numb):
    if numb < 20:
        if numb == 1:
            suffix = 'st'
        elif numb == 2:
            suffix = 'nd'
        elif numb == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    else:
        tens = str(numb)
        tens = tens[-2]
        unit = str(numb)
        unit = unit[-1]
        if tens == "1":
           suffix = "th"
        else:
            if unit == "1":
                suffix = 'st'
            elif unit == "2":
                suffix = 'nd'
            elif unit == "3":
                suffix = 'rd'
            else:
                suffix = 'th'
    return str(numb)+ suffix

def gradeLetter(grade):
    if grade >= 90.0:
        return "A"
    elif grade <= 80.0 <= 90.0:
        return "B"
    elif grade <= 70.0 <= 80.0:
        return "C"
    elif grade < 70.0:
        return "F"

print("Welcome to GradingSys")
count = 1
while(True):
    print("To start, enter your " + ord(count) + " grade.")
    grd = input("")
    if grd == "#avg":
        print("Your average grade is " + str(avg(grdList)))
        break
    elif grd == "#x":
        break
    elif grd == "#view":
        print(", ".join(map(str,grdList)))
    elif grd == "#letter":
        avg = avg(grdList)
        print("Your grade is " + gradeLetter(avg))
        break
    elif grd == "":
        print("Invalid Grade. ErrorCode: EmptyInput")
    else:
        try:
            grd = int(grd)
            if grd <= 100:
                grdList.append(grd)
                count += 1
            else:
                print("Grade larger than 100.")
        except ValueError:
            print("Invalid Grade. ErrorCode: NotInteger")
