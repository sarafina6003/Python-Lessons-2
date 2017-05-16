while True:
    age = input("Enter your age: ")
    age = int(age)

    if age <5 :
        print ("This is a toddler :"+str(age))
    elif age >=6 and age<=12:
        print ("This is a kid :"+str(age))
    elif age >=13 and age<=20:
        print ("This is a teenager :"+str(age))
    elif age >=21 and age<=35:
        print ("This is a youth :"+str(age))
    elif age >=36 and age<=55:
        print ("This is a middle age :"+str(age))
    else:
        print ("This is a senior citizen :"+str(age))
