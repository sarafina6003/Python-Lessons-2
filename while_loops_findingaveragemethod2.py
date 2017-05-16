count =0
total =0

while True:
    entry = input("Enter a mark: ")
    if entry == "AVG":
        break
    mark = int(entry)
    total +=mark
    count +=1
average= total/count
print("The average is "+ str(average))